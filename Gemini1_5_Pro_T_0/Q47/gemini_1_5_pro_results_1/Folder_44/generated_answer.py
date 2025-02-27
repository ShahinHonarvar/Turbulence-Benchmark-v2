def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 99):
        for j in range(i + 31 - 1, min(i + 51, 99)):
            substring = text[i:j]
            if len(substring) >= 31 and len(substring) <= 51 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes