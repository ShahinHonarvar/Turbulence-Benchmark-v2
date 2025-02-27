def palindromes_between_indices(text):
    letters = text[3:7]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 4 and substring.lower() == substring[::-1].lower():
                palindromes.add(''.join(sorted(substring)))
    return palindromes