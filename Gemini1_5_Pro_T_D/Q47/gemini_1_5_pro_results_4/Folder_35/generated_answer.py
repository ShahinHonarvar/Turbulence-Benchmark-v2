def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(34, 91):
        for j in range(14, 40):
            if i + j <= 91:
                substring = text[i:i + j]
                if len(substring) >= 14 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                    palindromes.add(substring)
    return palindromes