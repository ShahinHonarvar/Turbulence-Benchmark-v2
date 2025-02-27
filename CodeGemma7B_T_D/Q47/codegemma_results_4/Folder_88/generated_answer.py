def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(11, 88):
        for j in range(i + 4, i + 6):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes