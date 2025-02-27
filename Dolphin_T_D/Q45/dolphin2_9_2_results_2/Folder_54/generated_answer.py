def palindromes_between_indices(s):
    letters = [c.lower() for c in list(s[4:10]) if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes