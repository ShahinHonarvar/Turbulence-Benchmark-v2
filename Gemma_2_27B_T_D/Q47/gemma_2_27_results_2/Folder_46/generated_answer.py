def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i, min(i + 62, 98)):
            substring = text[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower() and (29 <= len(substring) <= 62):
                palindromes.add(substring)
    return palindromes