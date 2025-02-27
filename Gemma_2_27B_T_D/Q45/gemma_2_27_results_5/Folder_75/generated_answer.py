def palindromes_between_indices(text):
    letters = text[2:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1].lower()
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes