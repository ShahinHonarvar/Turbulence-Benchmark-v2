def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(31):
        for j in range(i + 1, 31):
            substring = text[i:j].lower()
            if 20 <= len(substring) <= 30 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes