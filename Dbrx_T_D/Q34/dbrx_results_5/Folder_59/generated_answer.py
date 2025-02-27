def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10):
    all_sets = [set1, set2, set3, set4, set5, set6, set7, set8, set9, set10]
    original_set = set()
    for element in all_sets:
        original_set.update(element)
    return original_set