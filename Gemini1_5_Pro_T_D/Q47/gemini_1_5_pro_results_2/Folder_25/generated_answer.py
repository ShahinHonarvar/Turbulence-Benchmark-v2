def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 85):
        for j in range(i + 30, min(i + 47, 85)):
            substring = text[i:j]
            if len(substring) >= 30 and len(substring) <= 46 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes