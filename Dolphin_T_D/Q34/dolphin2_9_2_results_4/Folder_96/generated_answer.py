def find_original_set(*sets):
    merged_set = {}
    for s in sets:
        for num in s:
            if num not in merged_set:
                merged_set[num] = 1
    return sorted(list(merged_set.keys()))