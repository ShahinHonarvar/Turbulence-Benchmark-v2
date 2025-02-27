def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 99):
        for j in range(i, min(i + 51, 99)):
            substring = text[i:j + 1]
            if len(substring) >= 31 and len(substring) <= 51 and (substring.lower() == substring.lower()[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes