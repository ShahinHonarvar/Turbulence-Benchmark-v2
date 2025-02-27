def palindromes_of_specific_lengths(str):
    s = str.lower()
    ps = set()
    for i in range(0, 9):
        for j in range(i + 1, min(i + 6, len(s))):
            if s[i] == s[j]:
                for k in range(j + 1, min(j + 3, len(s))):
                    if s[k] == s[j]:
                        ps.add(s[i:k + 1])
    return ps