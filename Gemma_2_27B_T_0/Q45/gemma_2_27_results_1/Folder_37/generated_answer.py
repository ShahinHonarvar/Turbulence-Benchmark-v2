def palindromes_between_indices(text):
    letters = text[1:5].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes