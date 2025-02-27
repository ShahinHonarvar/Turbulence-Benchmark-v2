def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 99):
        for j in range(i + 15, min(i + 26, 99)):
            substring = text[i:j + 1]
            if len(substring) >= 31 and len(substring) <= 51 and (substring.lower() == substring[::-1].lower()) and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes