def find_subset_of_length_n(s):
    if len(s) < 8:
        return 0
    subset_count = 0
    for i in range(len(s)):
        if i > len(s) - 8:
            break
        subset = set()
        for j in range(i, len(s)):
            subset.add(s[j])
            if len(subset) > 8:
                break
            if len(subset) == 8:
                subset_count += 1
    return subset_count