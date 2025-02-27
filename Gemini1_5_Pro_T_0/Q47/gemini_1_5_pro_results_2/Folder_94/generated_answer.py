def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(40, 95):
        for j in range(i + 45, min(i + 52, 95)):
            substring = text[i:j]
            if len(substring) >= 45 and len(substring) <= 51 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes