def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 98):
        for j in range(i + 6, min(i + 10, 99)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes