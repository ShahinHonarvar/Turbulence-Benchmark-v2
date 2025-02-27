def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    master_set = set()
    for arg in (set1, set2, set3, set4, set5, set6, set7, set8):
        master_set.update(arg)
    return master_set