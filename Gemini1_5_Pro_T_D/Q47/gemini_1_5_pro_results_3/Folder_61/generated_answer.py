def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(0, 31):
        for j in range(i, 31):
            substring = text[i:j + 1]
            if 20 <= len(substring) <= 30 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes