def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 52):
        for j in range(i + 1, len(s) - 51):
            for k in range(j + 1, len(s) - 50):
                for l in range(k + 1, len(s) - 49):
                    for m in range(l + 1, len(s) - 48):
                        for n in range(m + 1, len(s) - 47):
                            for o in range(n + 1, len(s) - 46):
                                for p in range(o + 1, len(s) - 45):
                                    for q in range(p + 1, len(s) - 44):
                                        for r in range(q + 1, len(s) - 43):
                                            for s in range(r + 1, len(s) - 42):
                                                for t in range(s + 1, len(s) - 41):
                                                    for u in range(t + 1, len(s) - 40):
                                                        for v in range(u + 1, len(s) - 39):
                                                            for w in range(v + 1, len(s) - 38):
                                                                for x in range(w + 1, len(s) - 37):
                                                                    for y in range(x + 1, len(s) - 36):
                                                                        for z in range(y + 1, len(s) - 35):
                                                                            if s[i] == s[j] == s[k] == s[l] == s[m] == s[n] == s[o] == s[p] == s[q] == s[r] == s[s] == s[t] == s[u] == s[v] == s[w] == s[x] == s[y] == s[z] == s[i + 26] == s[j + 26] == s[k + 26] == s[l + 26] == s[m + 26] == s[n + 26] == s[o + 26] == s[p + 26] == s[q + 26] == s[r + 26] == s[s + 26] == s[t + 26] == s[u + 26] == s[v + 26] == s[w + 26] == s[x + 26] == s[y + 26] == s[z + 26]:
                                                                                palindromes.add(s[i:j + 1])
    return palindromes