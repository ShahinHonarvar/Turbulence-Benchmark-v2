def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10):
        for j in range(i + 1, min(i + 6, 11)):
            substring = text[i:j].lower()
            if len(substring) >= 3 and len(substring) <= 5 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes