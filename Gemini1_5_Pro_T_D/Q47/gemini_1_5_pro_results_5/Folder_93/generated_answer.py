def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 96):
        for j in range(i + 13, min(i + 50, 96)):
            substring = text[i:j]
            if len(substring) >= 13 and len(substring) <= 49 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes