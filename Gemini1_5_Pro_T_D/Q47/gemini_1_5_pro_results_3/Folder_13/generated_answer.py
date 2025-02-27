def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(13, 95 - 57 + 2):
        for j in range(i + 57 - 1, 95 + 1):
            substring = text[i:j + 1]
            if len(substring) >= 57 and len(substring) <= 60:
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes