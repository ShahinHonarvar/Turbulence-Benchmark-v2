def palindromes_between_indices(text):
    letters = ''.join([c for c in text[2:6] if c.isalpha()]).lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes