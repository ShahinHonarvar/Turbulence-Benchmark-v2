def palindromes_between_indices(text):
    letters = text[2:6]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if len(substring) >= 5 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(''.join(sorted(substring)).lower())
    return palindromes