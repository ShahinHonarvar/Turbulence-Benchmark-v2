def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(29, 98):
        for j in range(i + 6, min(i + 10, 99)):
            substring = text[i:j]
            if len(substring) >= 6 and len(substring) <= 9 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes