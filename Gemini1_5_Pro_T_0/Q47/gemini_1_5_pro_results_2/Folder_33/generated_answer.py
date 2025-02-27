def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(130, 296):
        for j in range(i + 102, min(i + 158, 296) + 1):
            substring = text[i:j + 1]
            if len(substring) >= 103 and len(substring) <= 158 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes