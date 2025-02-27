def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 72):
        for j in range(i, 73):
            substring = text[i:j + 1]
            if 19 <= len(substring) <= 55 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes