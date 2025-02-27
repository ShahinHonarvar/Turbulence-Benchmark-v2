def find_subset_of_length_n(s):
    result = 0
    for i in range(2 ** len(s)):
        subset = set()
        for j in range(len(s)):
            if i & 1 << j:
                subset.add(s[j])
        if len(subset) == 100:
            result += 1
    return result