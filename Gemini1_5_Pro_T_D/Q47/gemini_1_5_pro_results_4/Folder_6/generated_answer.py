def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 98 - 39):
        for j in range(i + 39, 99):
            substring = text[i:j]
            if len(substring) >= 40 and len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes