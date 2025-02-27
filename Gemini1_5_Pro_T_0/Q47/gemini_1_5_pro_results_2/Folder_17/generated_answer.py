def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 95 - 51):
        for j in range(i + 52, min(i + 56, 96)):
            substring = text[i:j]
            if len(substring) >= 52 and len(substring) <= 55 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes