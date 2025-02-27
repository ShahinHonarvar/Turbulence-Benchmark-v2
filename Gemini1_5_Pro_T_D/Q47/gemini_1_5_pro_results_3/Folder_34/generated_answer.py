def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(200, 301):
        for j in range(i, 301):
            substring = text[i:j + 1].lower()
            if 10 <= len(substring) <= 50 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes