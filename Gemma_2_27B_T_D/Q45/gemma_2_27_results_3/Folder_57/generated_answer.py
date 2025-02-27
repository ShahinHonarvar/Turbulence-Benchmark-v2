def palindromes_between_indices(text):
    letters = text[2:6].lower()
    palindromes = set()
    for i in range(len(letters) - 4):
        for j in range(i + 5, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes