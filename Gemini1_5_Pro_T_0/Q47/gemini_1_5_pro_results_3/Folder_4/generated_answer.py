def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(12, 92 - 16):
        for j in range(i + 17, 93):
            substring = text[i:j]
            if 17 <= len(substring) <= 66 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes