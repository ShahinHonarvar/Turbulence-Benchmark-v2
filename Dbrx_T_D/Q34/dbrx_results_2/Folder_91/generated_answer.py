def find_original_set(set_1, set_2, set_3, set_4, set_5):
    all_sets = [set_1, set_2, set_3, set_4, set_5]
    original_set = set()
    for element in all_sets:
        original_set.update(element)
    return original_set