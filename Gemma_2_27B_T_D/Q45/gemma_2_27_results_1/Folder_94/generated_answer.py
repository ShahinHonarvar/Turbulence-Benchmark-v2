def palindromes_between_indices(text):
    letters = text[3:5].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes