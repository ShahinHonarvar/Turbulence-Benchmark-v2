def find_original_set(set1, set2, set3, set4):
    all_sets = [set1, set2, set3, set4]
    original_set = set()
    for num in set1:
        if num in original_set:
            continue
        for other_set in all_sets[1:]:
            if num not in other_set:
                break
        else:
            original_set.add(num)
    return original_set