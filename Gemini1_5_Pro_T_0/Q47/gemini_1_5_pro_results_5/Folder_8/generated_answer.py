def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 73):
        for j in range(i + 49, min(i + 51, 73)):
            substring = text[i:j + 1]
            if len(substring) >= 50 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes