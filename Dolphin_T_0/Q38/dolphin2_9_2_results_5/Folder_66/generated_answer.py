def find_subset_of_length_n(s):
    if len(s) < 42:
        return 0
    count = 0
    for i in range(len(s)):
        subset = [s[i]]
        for j in range(i + 1, len(s)):
            subset.append(s[j])
            if len(subset) == 42:
                count += 1
            elif len(subset) > 42:
                break
    return count