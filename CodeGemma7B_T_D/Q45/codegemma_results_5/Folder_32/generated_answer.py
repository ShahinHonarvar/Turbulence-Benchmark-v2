def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 4, 8):
            substring = text[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes