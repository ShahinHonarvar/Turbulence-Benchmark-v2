def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(2, 5):
        for j in range(i + 1, 6):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes