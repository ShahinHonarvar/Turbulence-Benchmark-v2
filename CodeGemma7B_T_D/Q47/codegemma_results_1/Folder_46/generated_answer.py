def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i + 29, i + 63):
            substring = text[i:j + 1].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes