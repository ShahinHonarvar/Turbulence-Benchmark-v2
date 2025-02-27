def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 201):
        for j in range(i, min(i + 10, 201)):
            substring = text[i:j + 1]
            if len(substring) >= 5 and len(substring) <= 10 and (substring.lower() == substring.lower()[::-1]) and substring.isalpha():
                palindromes.add(substring)
    return palindromes