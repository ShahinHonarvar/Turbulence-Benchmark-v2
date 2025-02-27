def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i + 136, min(i + 161, 296)):
            substring = text[i:j]
            if len(substring) >= 136 and len(substring) <= 160 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes