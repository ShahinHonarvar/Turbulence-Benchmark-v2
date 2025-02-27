def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 59):
        for j in range(i + 1, len(text) - 59):
            for k in range(j + 1, len(text) - 59):
                for l in range(k + 1, len(text) - 59):
                    for m in range(l + 1, len(text) - 59):
                        for n in range(m + 1, len(text) - 59):
                            for o in range(n + 1, len(text) - 59):
                                for p in range(o + 1, len(text) - 59):
                                    for q in range(p + 1, len(text) - 59):
                                        for r in range(q + 1, len(text) - 59):
                                            for s in range(r + 1, len(text) - 59):
                                                for t in range(s + 1, len(text) - 59):
                                                    for u in range(t + 1, len(text) - 59):
                                                        for v in range(u + 1, len(text) - 59):
                                                            for w in range(v + 1, len(text) - 59):
                                                                for x in range(w + 1, len(text) - 59):
                                                                    for y in range(x + 1, len(text) - 59):
                                                                        for z in range(y + 1, len(text) - 59):
                                                                            if text[i] == text[j] and text[j] == text[k] and (text[k] == text[l]) and (text[l] == text[m]) and (text[m] == text[n]) and (text[n] == text[o]) and (text[o] == text[p]) and (text[p] == text[q]) and (text[q] == text[r]) and (text[r] == text[s]) and (text[s] == text[t]) and (text[t] == text[u]) and (text[u] == text[v]) and (text[v] == text[w]) and (text[w] == text[x]) and (text[x] == text[y]) and (text[y] == text[z]):
                                                                                palindromes.add(text[i:z + 1])
    return palindromes