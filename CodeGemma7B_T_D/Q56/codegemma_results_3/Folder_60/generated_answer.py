from itertools import permutations

def all_substring_of_size_n(s):
    if len(s) < 36:
        return []
    result = set()
    for i in range(len(s) - 35):
        for j in range(i + 1, len(s) - 34):
            for k in range(j + 1, len(s) - 33):
                for l in range(k + 1, len(s) - 32):
                    for m in range(l + 1, len(s) - 31):
                        for n in range(m + 1, len(s) - 30):
                            for o in range(n + 1, len(s) - 29):
                                for p in range(o + 1, len(s) - 28):
                                    for q in range(p + 1, len(s) - 27):
                                        for r in range(q + 1, len(s) - 26):
                                            for s in range(r + 1, len(s) - 25):
                                                for t in range(s + 1, len(s) - 24):
                                                    for u in range(t + 1, len(s) - 23):
                                                        for v in range(u + 1, len(s) - 22):
                                                            for w in range(v + 1, len(s) - 21):
                                                                for x in range(w + 1, len(s) - 20):
                                                                    for y in range(x + 1, len(s) - 19):
                                                                        for z in range(y + 1, len(s) - 18):
                                                                            for aa in range(z + 1, len(s) - 17):
                                                                                if len(set([s[i], s[j], s[k], s[l], s[m], s[n], s[o], s[p], s[q], s[r], s[s], s[t], s[u], s[v], s[w], s[x], s[y], s[z], aa])) == 26:
                                                                                    result.add(''.join(p))
    return list(result)