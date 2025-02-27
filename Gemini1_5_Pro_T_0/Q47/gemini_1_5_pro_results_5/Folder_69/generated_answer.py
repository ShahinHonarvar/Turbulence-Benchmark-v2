def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 96 - 44):
        for j in range(i + 44, 97):
            substring = text[i:j + 1]
            if 45 <= len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes