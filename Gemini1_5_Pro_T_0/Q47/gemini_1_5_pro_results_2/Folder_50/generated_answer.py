def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(36, 93):
        for j in range(i + 9, min(93, i + 36)):
            substring = text[i:j]
            if len(substring) >= 10 and len(substring) <= 35 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes