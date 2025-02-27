def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters) - 1):
                for l in range(k + 1, len(letters)):
                    p = letters[i] + letters[j] + letters[k] + letters[l]
                    if p == p[::-1]:
                        palindromes.add(p)
    return palindromes