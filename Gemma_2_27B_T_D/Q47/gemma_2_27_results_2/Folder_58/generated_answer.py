def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(125, 284):
        for j in range(i, 284):
            substring = text[i:j + 1]
            if len(substring) >= 109 and len(substring) <= 126 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes