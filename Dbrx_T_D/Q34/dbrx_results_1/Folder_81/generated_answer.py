def find_original_set(input_sets):
    input_sets = sorted(input_sets, key=lambda s: len(s))
    result_set = set()
    for current_set in input_sets:
        result_set.update(current_set.difference(result_set))
    return result_set