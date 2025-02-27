def find_subset_of_length_n(s):
    n = 18
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s)):
                    for m in range(l + 1, len(s)):
                        for o in range(m + 1, len(s)):
                            for p in range(o + 1, len(s)):
                                for q in range(p + 1, len(s)):
                                    for r in range(q + 1, len(s)):
                                        for t in range(r + 1, len(s)):
                                            for u in range(t + 1, len(s)):
                                                for v in range(u + 1, len(s)):
                                                    if len({s[i], s[j], s[k], s[l], s[m], s[o], s[p], s[q], s[r], s[t], s[u], s[v], s[w], s[x], s[y], s[z], s[aa], s[bb]}) == n:
                                                        count += 1
    return count