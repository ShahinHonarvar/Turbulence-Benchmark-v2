def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 88):
        for j in range(i + 38, min(i + 61, 88)):
            substring = text[i:j]
            if len(substring) >= 38 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes