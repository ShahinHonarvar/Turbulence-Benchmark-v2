def palindromes_between_indices(s):
    letters = ''.join([c for c in s[4:9] if c.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes