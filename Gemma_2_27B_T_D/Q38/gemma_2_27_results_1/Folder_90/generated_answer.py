def find_subset_of_length_n(s):
    n = 752
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    for m in range(l + 1, len(s)):
                        for p in range(m + 1, len(s)):
                            for q in range(p + 1, len(s)):
                                for r in range(q + 1, len(s)):
                                    if len({s[i], s[j], s[k], s[l], s[m], s[p], s[q], s[r]}) == n:
                                        count += 1
    return count