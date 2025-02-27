def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 94 - 37):
        for j in range(i + 38, min(i + 50, 95)):
            substring = text[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes