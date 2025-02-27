def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes