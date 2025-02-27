def palindromes_between_indices(s):
    letters = [c for c in s[6:9] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes