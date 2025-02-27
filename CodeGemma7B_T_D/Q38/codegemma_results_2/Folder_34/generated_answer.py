def find_subset_of_length_n(s):
    result = 0
    for i in range(2 ** len(s)):
        subset = []
        for j in range(len(s)):
            if i >> j & 1:
                subset.append(s[j])
        if len(subset) == 97:
            result += 1
    return result