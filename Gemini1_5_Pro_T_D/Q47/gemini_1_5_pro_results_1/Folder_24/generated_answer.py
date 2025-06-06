def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 93):
        for j in range(i + 41, min(i + 77, 93) + 1):
            substring = text[i:j]
            if len(substring) >= 42 and len(substring) <= 77 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes