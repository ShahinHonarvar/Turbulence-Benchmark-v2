def palindromes_between_indices(text):
    letters = ''.join((c for c in text[5:10] if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 4, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes