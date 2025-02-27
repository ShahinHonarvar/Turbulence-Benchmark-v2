def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(130, 295 - 103 + 2):
        for j in range(i + 103, min(i + 159, 296)):
            substring = text[i:j]
            if len(substring) >= 103 and len(substring) <= 158 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes