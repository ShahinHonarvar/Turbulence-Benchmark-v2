def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(119, 257):
        for j in range(i, 257):
            substring = text[i:j + 1]
            if 104 <= len(substring) <= 123 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes