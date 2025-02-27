def palindromes_between_indices(text):
    letters = text[5:7].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes