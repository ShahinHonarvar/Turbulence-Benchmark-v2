def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(127, 289):
        for j in range(i + 118, min(289, i + 141) + 1):
            substring = text[i:j]
            if len(substring) >= 119 and len(substring) <= 141 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes