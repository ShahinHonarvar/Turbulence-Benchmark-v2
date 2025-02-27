def palindromes_between_indices(text):
    letters = text[1:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 3 and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes