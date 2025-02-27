def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 56 - 19):
        for j in range(i + 20, min(i + 22, 57)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes