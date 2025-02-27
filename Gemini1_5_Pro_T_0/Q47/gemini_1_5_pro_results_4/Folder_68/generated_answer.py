def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(51):
        for j in range(i + 50, min(i + 101, 51)):
            substring = text[i:j]
            if len(substring) >= 50 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes