def find_subset_of_length_n(s):
    n = 630
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    for m in range(l + 1, len(s)):
                        for o in range(m + 1, len(s)):
                            if len({s[i], s[j], s[k], s[l], s[m], s[o]}) == n:
                                count += 1
    return count