def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83):
        for j in range(i + 36, min(i + 60, 84) + 1):
            substring = text[i:j]
            if len(substring) >= 37 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes