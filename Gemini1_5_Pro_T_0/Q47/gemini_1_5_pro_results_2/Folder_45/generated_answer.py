def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(70, 141):
        for j in range(i + 3, min(141, i + 61)):
            substring = text[i:j]
            if len(substring) >= 3 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes