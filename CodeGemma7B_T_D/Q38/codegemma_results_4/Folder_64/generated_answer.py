def find_subset_of_length_n(s):
    cases = 2 ** len(s)
    with_n = 0
    for b in range(cases):
        subset = []
        for i in range(len(s)):
            if b & 1 << i:
                subset.append(s[i])
        if len(subset) == 1:
            with_n += 1
    return with_n