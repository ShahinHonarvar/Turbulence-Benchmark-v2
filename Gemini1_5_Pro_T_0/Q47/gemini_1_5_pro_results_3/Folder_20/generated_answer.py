def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(20, 75):
        for j in range(i + 36, min(i + 43, 75)):
            substring = text[i:j]
            if len(substring) >= 36 and len(substring) <= 42 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes