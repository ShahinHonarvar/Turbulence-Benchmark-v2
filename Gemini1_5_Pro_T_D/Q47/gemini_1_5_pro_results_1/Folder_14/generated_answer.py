def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 74):
        for j in range(i + 6, min(i + 9, 75)):
            substring = text[i:j]
            if len(substring) >= 6 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring.lower())
    return palindromes