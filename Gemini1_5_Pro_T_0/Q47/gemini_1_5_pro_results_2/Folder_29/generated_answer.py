def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 95):
        for j in range(i + 18, min(i + 74, 95)):
            substring = text[i:j]
            if len(substring) >= 18 and len(substring) <= 73 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes