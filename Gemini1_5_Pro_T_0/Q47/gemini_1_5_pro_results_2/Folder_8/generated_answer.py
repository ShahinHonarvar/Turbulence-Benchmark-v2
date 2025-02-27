def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(17, 72 - 49):
        for j in range(i + 50, i + 52):
            substring = text[i:j]
            if len(substring) >= 50 and len(substring) <= 51 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes