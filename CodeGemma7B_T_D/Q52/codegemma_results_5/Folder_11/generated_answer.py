def palindrome_of_length_n(s: str) -> set:
    L = list(set(s.lower()))
    L.sort()
    res = set()
    for i in range(len(L) - 8):
        for j in range(i + 1, len(L) - 6):
            for k in range(j + 1, len(L) - 4):
                for l in range(k + 1, len(L) - 2):
                    for m in range(l + 1, len(L) - 1):
                        for n in range(m + 1, len(L)):
                            s = ''.join(L[i:n + 1])
                            if s == s[::-1]:
                                res.add(s)
    return res