def palindromes_between_indices(s):
    s = s[1:5].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes