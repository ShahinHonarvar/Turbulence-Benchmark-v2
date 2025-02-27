def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring).lower())
    return palindromes