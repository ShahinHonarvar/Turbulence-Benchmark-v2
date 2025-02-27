def palindromes_between_indices(s):
    substring = s[5:8]
    letters = [c.lower() for c in substring if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub = ''.join(letters[i:j])
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes