def palindromes_between_indices(text):
    letters = text[2:6].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 4:
                palindromes.add(''.join(sorted(substring)))
    return palindromes