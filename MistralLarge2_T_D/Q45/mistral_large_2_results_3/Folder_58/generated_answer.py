def palindromes_between_indices(s):
    letters = [c for c in s[:7] if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            substring = ''.join(letters[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes