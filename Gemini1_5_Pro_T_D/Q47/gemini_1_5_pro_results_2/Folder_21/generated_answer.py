def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i + 135, min(i + 161, 296)):
            substring = text[i:j + 1]
            if len(substring) >= 136 and len(substring) <= 160 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes