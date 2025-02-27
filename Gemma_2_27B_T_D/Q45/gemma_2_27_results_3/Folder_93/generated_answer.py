def palindromes_between_indices(text):
    letters = text[2:8]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 6 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes