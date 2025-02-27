def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 7, len(letters) + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(''.join(sub))
    return palindromes