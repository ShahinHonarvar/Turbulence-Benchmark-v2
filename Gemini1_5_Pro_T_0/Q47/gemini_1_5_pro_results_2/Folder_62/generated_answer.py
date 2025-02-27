def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 88):
        for j in range(i + 51, min(i + 57, 88)):
            substring = text[i:j]
            if len(substring) >= 52 and len(substring) <= 56 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes