def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 65):
        for j in range(i + 27, 91):
            substring = text[i:j].lower()
            if 27 <= len(substring) <= 58 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes