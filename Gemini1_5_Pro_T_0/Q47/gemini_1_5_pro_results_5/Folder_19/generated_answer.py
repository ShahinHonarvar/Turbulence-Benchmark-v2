def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 56):
        for j in range(i + 3, min(i + 8, 56)):
            substring = text[i:j]
            if len(substring) >= 3 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring.lower())
    return palindromes