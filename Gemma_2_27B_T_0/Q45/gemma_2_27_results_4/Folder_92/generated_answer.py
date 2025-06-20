def palindromes_between_indices(text):
    letters = text[4:8].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes