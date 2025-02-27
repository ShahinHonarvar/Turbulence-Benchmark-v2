def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text) - 406):
        for j in range(i + 1, len(text) - 405):
            for k in range(j + 1, len(text) - 404):
                for l in range(k + 1, len(text) - 403):
                    for m in range(l + 1, len(text) - 402):
                        for n in range(m + 1, len(text) - 401):
                            for o in range(n + 1, len(text) - 400):
                                for p in range(o + 1, len(text) - 399):
                                    for q in range(p + 1, len(text) - 398):
                                        for r in range(q + 1, len(text) - 397):
                                            for s in range(r + 1, len(text) - 396):
                                                for t in range(s + 1, len(text) - 395):
                                                    for u in range(t + 1, len(text) - 394):
                                                        for v in range(u + 1, len(text) - 393):
                                                            for w in range(v + 1, len(text) - 392):
                                                                for x in range(w + 1, len(text) - 391):
                                                                    for y in range(x + 1, len(text) - 390):
                                                                        for z in range(y + 1, len(text) - 389):
                                                                            if text[i:i + 407] == text[i:i + 407][::-1]:
                                                                                palindromes.add(text[i:i + 407])
    return palindromes