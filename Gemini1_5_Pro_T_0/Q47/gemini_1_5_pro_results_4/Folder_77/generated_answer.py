def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(103, 276):
        for j in range(i + 100, min(i + 170, 277)):
            substring = text[i:j]
            if len(substring) >= 100 and len(substring) <= 169 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes