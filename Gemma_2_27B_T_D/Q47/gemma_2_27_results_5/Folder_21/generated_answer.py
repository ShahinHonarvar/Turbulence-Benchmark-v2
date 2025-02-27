def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i, 296):
            substring = text[i:j + 1]
            if len(substring) >= 136 and len(substring) <= 160 and (substring.lower() == substring.lower()[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes