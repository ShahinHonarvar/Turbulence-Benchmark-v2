def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i + 12, min(84, i + 56)):
            substring = text[i:j]
            if len(substring) >= 13 and len(substring) <= 66 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes