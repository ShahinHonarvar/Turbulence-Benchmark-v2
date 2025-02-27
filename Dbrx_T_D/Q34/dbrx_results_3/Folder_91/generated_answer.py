def find_original_set(set1, set2, set3, set4, set5):
    all_sets = [set1, set2, set3, set4, set5]
    original_set = set()
    for current_set in all_sets:
        original_set.update(current_set)
    return original_set