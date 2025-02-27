def palindromes_between_indices(text):
    letters = text[7:10].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes