def palindromes_between_indices(s):
    s = s[8:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for c in letters:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    p = c + letters[i] + letters[j] + letters[k] + c
                    if p == p[::-1]:
                        palindromes.add(p)
    return palindromes