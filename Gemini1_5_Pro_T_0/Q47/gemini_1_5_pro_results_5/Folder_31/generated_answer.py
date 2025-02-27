def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83 - 36):
        for j in range(i + 37, min(i + 61, 84)):
            substring = text[i:j]
            if len(substring) >= 37 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes