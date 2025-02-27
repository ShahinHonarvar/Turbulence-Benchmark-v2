def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 96 - 44):
        for j in range(i + 45, min(i + 53, 97)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes