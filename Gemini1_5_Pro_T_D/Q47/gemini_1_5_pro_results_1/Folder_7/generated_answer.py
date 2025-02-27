def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(119, 257):
        for j in range(i + 103, min(257, i + 124)):
            substring = text[i:j]
            if len(substring) >= 104 and len(substring) <= 123 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes