def palindromes_of_specific_lengths(text):
    text_lowercase = text.lower()
    palindromes = set()
    for i in range(21, 63):
        for j in range(i + 22, i + 34):
            substring = text_lowercase[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes