def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(6):
        for j in range(i + 3, 7):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes