def palindromes_between_indices(text):
    letters = sorted([c for c in text[:5] if c.isalpha()])
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 4, len(letters)):
            substring = ''.join(letters[i:j + 1])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes