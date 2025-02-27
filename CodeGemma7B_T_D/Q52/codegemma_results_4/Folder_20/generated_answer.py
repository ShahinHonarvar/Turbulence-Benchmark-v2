def palindrome_of_length_n(str):
    str_lower = str.lower()
    palindrome_set = set()
    for i in range(len(str_lower)):
        for j in range(i + 1, len(str_lower)):
            for k in range(j + 1, len(str_lower)):
                for l in range(k + 1, len(str_lower)):
                    for m in range(l + 1, len(str_lower)):
                        for n in range(m + 1, len(str_lower)):
                            for o in range(n + 1, len(str_lower)):
                                for p in range(o + 1, len(str_lower)):
                                    for q in range(p + 1, len(str_lower)):
                                        for r in range(q + 1, len(str_lower)):
                                            for s in range(r + 1, len(str_lower)):
                                                for t in range(s + 1, len(str_lower)):
                                                    for u in range(t + 1, len(str_lower)):
                                                        for v in range(u + 1, len(str_lower)):
                                                            for w in range(v + 1, len(str_lower)):
                                                                for x in range(w + 1, len(str_lower)):
                                                                    for y in range(x + 1, len(str_lower)):
                                                                        for z in range(y + 1, len(str_lower)):
                                                                            substring = str_lower[i:i + 53]
                                                                            if substring == substring[::-1]:
                                                                                palindrome_set.add(substring)
    return palindrome_set