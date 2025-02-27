def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(101, 292 - 154 + 2):
        for j in range(i + 154 - 1, min(292 + 1, i + 182)):
            substring = text[i:j + 1]
            if len(substring) >= 154 and len(substring) <= 182 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes