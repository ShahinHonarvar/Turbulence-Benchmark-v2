def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 8):
        for j in range(i + 2, 8):
            substring = text[i:j]
            if substring == substring[::-1] and len(substring) in range(3, 5):
                palindromes.add(substring)
    return palindromes