def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 99 - 25):
        for j in range(i + 25, min(100, i + 30)):
            substring = text[i:j]
            if len(substring) >= 26 and len(substring) <= 29 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes