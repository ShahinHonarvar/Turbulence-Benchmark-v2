def palindromes_between_indices(text):
    letters = text[3:7].lower()
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes