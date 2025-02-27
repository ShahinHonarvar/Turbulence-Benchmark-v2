def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 83):
        for j in range(i + 13, min(i + 67, 84)):
            substring = text[i:j]
            if len(substring) >= 13 and len(substring) <= 66 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes