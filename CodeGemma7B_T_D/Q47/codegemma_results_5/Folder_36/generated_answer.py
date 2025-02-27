def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(124, 284):
        for j in range(i, 284):
            substring = text[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 115 and (len(substring) <= 134):
                palindromes.add(substring)
    return palindromes