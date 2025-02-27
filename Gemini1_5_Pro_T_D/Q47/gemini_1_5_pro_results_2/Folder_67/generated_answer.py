def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(65, 99 + 1):
        for j in range(i, 99 + 1):
            substring = text[i:j + 1]
            if 26 <= len(substring) <= 33 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes