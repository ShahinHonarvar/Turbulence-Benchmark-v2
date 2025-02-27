def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 99):
        for j in range(i, 99):
            substring = text[i:j + 1]
            if 40 <= len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes