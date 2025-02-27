def palindromes_between_indices(text):
    letters = text[6:10].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if substring[::-1] == substring:
                palindromes.add(substring)
    return palindromes