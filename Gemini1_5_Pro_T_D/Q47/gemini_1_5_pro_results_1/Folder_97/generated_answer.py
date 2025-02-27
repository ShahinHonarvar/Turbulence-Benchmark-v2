def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 94 + 1 - 38):
        for j in range(i + 38, min(94 + 1, i + 50)):
            substring = text[i:j]
            if len(substring) >= 38 and len(substring) <= 49 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes