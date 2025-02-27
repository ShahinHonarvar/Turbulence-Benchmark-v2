def find_subset_of_length_n(s):
    if len(s) < 6:
        return 0
    subset_count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for m in range(k + 1, len(s)):
                    for n in range(m + 1, len(s)):
                        for o in range(n + 1, len(s)):
                            subset = {s[i], s[j], s[k], s[m], s[n], s[o]}
                            if len(subset) == 6:
                                subset_count += 1
    return subset_count