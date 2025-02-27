def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i + 9, i + 37):
            substring = text[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1] and (10 <= len(substring) <= 36):
                palindromes.add(substring)
    return palindromes