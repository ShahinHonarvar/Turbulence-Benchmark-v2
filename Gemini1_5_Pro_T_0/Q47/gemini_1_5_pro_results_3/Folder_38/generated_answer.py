def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 88):
        for j in range(i + 18, min(i + 31, 88)):
            substring = text[i:j + 1]
            if 38 <= len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes