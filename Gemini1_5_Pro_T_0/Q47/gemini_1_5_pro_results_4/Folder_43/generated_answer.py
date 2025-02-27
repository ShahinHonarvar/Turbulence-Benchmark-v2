def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(41, 90):
        for j in range(i + 23, min(i + 39, 90)):
            substring = text[i:j]
            if len(substring) >= 23 and len(substring) <= 38 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes