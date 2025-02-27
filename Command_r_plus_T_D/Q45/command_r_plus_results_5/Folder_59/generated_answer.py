def palindromes_between_indices(s):
    letters = [c for c in s[8:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes