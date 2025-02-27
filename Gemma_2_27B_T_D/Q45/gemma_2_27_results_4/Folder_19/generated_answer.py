def palindromes_between_indices(text):
    letters = text[1:8].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j]
            if substring == substring[::-1] and len(substring) >= 7:
                palindromes.add(substring)
    return palindromes