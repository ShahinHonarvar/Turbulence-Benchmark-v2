def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 87):
        for j in range(i + 50, min(i + 60, 87)):
            substring = text[i:j + 1]
            if len(substring) >= 51 and len(substring) <= 60 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes