def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 56 - 19):
        for j in range(i + 19, 57):
            substring = text[i:j]
            if len(substring) >= 20 and len(substring) <= 21 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes