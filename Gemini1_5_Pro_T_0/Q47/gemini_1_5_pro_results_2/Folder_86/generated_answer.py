def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(30, 96):
        for j in range(i + 34, min(i + 56, 96)):
            substring = text[i:j]
            if len(substring) >= 34 and len(substring) <= 55 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes