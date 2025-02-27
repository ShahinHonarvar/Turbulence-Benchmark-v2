def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(0, 8):
        for j in range(i + 4, min(i + 6, 8)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes