def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(32, 71 - 20):
        for j in range(i + 21, 72):
            substring = text[i:j]
            if len(substring) >= 21 and len(substring) <= 32 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes