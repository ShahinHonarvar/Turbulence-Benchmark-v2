def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[7:9] if c.isalpha()))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes