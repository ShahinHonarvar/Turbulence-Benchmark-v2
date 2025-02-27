def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 56):
        for j in range(i + 3, min(56, i + 8)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes