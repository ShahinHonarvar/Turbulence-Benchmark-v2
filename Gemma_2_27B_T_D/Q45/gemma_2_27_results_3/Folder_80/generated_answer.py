def palindromes_between_indices(text):
    letters = text[3:9]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1].lower()
            if len(substring) >= 7 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes