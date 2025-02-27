def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for a in range(k + 1, len(letters)):
                    for b in range(a + 1, len(letters)):
                        for c in range(b + 1, len(letters)):
                            for d in range(c + 1, len(letters)):
                                p1 = letters[i] + letters[j] + letters[k] + letters[a] + letters[b] + letters[c] + letters[d] + letters[c] + letters[b] + letters[a] + letters[k] + letters[j] + letters[i]
                                p2 = letters[i] + letters[j] + letters[k] + letters[a] + letters[b] + letters[c] + letters[d] + letters[d] + letters[c] + letters[b] + letters[a] + letters[k] + letters[j] + letters[i]
                                palindromes.add(p1)
                                palindromes.add(p2)
    return palindromes