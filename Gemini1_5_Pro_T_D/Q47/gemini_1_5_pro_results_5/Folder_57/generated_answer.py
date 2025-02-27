def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(16, 95):
        for j in range(i + 38, min(i + 52, 95)):
            substring = text[i:j + 1]
            if len(substring) >= 39 and len(substring) <= 52 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes