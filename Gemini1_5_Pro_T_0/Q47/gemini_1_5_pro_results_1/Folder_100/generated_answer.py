def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 97):
        for j in range(i + 11, min(97, i + 19)):
            substring = text[i:j]
            if len(substring) >= 12 and len(substring) <= 18 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes