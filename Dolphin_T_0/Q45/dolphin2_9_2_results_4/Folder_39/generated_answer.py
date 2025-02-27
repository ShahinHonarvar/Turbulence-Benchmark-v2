def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes