def find_subset_of_length_n(s):
    n = len(s)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    for m in range(l + 1, n):
                        for o in range(m + 1, n):
                            for p in range(o + 1, n):
                                for q in range(p + 1, n):
                                    for r in range(q + 1, n):
                                        for t in range(r + 1, n):
                                            for u in range(t + 1, n):
                                                for v in range(u + 1, n):
                                                    for w in range(v + 1, n):
                                                        for x in range(w + 1, n):
                                                            if len({s[i], s[j], s[k], s[l], s[m], s[o], s[p], s[q], s[r], s[t], s[u], s[v], s[w], s[x]}) == 93:
                                                                result += 1
    return result