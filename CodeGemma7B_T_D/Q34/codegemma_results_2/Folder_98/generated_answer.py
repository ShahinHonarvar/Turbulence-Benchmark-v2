def find_original_set(A, B, C, D, E, F, G, H, I):
    all_sets = [A, B, C, D, E, F, G, H, I]
    min_set = min(all_sets, key=len)
    for subset in all_sets:
        if subset not in all_sets[:]:
            if subset.issubset(min_set):
                min_set = subset
    return min_set