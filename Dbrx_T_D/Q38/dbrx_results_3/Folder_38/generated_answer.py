def find_subset_of_length_n(s):
    if not s or len(s) < 38:
        return 0
    subset_count = 0
    for i in range(len(s) - 37):
        for j in range(i + 1, len(s) - 36):
            current_set = list(s[i:j + 1])
            if len(current_set) == 38:
                subset_count += 1
    return subset_count