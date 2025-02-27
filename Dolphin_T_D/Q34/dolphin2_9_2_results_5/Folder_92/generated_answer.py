def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    result = set1.copy()
    for additional_set in [set2, set3, set4, set5, set6, set7, set8]:
        result = result.union(additional_set)
    return result