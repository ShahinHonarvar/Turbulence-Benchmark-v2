def palindromes_between_indices(text):
    letters = text[3:8]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 4 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes