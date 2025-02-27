def palindromes_of_specific_lengths(text):
    low_text = text.lower()
    palindromes = set()
    for i in range(2, 8):
        for j in range(i + 2, 8):
            substring = low_text[i:j]
            if substring == substring[::-1] and len(substring) in range(3, 5):
                palindromes.add(substring)
    return palindromes