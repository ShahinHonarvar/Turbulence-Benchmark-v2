def palindromes_between_indices(s):
    letters = [c for c in s[0:7] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes