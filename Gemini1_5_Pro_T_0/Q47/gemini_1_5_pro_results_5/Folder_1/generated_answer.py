def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i + 40, min(i + 73, 90)):
            substring = text[i:j]
            if len(substring) >= 40 and len(substring) <= 72 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes