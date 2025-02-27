def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(124, 284):
        for j in range(i + 115, min(i + 135, 284)):
            substring = text[i:j]
            if len(substring) >= 115 and len(substring) <= 134 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes