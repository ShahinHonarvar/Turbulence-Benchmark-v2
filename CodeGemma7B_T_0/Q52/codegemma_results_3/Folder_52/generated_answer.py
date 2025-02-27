def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 422):
        for j in range(i + 1, len(text) - 421):
            for k in range(j + 1, len(text) - 420):
                for l in range(k + 1, len(text) - 419):
                    for m in range(l + 1, len(text) - 418):
                        for n in range(m + 1, len(text) - 417):
                            for o in range(n + 1, len(text) - 416):
                                for p in range(o + 1, len(text) - 415):
                                    for q in range(p + 1, len(text) - 414):
                                        for r in range(q + 1, len(text) - 413):
                                            for s in range(r + 1, len(text) - 412):
                                                for t in range(s + 1, len(text) - 411):
                                                    for u in range(t + 1, len(text) - 410):
                                                        for v in range(u + 1, len(text) - 409):
                                                            for w in range(v + 1, len(text) - 408):
                                                                for x in range(w + 1, len(text) - 407):
                                                                    for y in range(x + 1, len(text) - 406):
                                                                        for z in range(y + 1, len(text) - 405):
                                                                            if text[i:i + 423] == text[i:i + 423][::-1]:
                                                                                palindromes.add(text[i:i + 423])
    return palindromes