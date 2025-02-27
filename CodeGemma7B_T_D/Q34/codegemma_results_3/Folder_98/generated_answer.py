def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9):
    original_set = set()
    for s in [set1, set2, set3, set4, set5, set6, set7, set8, set9]:
        for x in s:
            if x not in original_set:
                original_set.add(x)
    return original_set