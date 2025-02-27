def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 101):
        for j in range(i, 101):
            substring = text[i:j + 1]
            if 10 <= len(substring) <= 50 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes