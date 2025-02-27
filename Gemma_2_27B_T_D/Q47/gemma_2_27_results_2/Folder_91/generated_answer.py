def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11):
        for j in range(i, 11):
            substring = text[i:j + 1]
            if len(substring) in range(3, 6) and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes