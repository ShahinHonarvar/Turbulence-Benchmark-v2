def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes