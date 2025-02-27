def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 94):
        for j in range(i, 94):
            substring = text[i:j + 1]
            if len(substring) >= 34 and len(substring) <= 54 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes