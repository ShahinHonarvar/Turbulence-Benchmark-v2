def palindromes_between_indices(s):
    letters = [c for c in s[4:7] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    letters_lower = [c.lower() for c in letters]
    for i in range(len(letters_lower)):
        for j in range(i + 3, len(letters_lower) + 1):
            substring = letters_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes