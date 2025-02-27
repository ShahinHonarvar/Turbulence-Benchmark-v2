def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281 - 136 + 1):
        for j in range(i + 136, 281 + 1):
            substring = text[i:j].lower()
            if len(substring) >= 136 and len(substring) <= 151 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes