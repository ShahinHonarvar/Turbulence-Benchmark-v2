def palindromes_between_indices(text):
    letters = ''.join([i.lower() for i in text[0:5] if i.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                palindromes.add(substring)
    return palindromes