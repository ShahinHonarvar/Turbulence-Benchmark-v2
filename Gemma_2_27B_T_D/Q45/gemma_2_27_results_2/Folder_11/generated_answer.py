def palindromes_between_indices(text):
    letters = text[3:8].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 4:
                palindromes.add(substring)
    return palindromes