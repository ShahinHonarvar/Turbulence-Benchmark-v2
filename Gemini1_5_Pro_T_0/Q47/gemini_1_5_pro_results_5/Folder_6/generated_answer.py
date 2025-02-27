def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(45, 99):
        for j in range(i + 39, min(99, i + 48)):
            substring = text[i:j]
            if len(substring) >= 40 and len(substring) <= 47 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes