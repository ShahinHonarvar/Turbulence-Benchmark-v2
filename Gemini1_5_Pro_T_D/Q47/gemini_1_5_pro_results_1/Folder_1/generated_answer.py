def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i + 39, min(90, i + 73)):
            substring = text[i:j]
            if len(substring) >= 40 and len(substring) <= 72 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes