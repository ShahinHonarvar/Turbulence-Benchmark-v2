def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes