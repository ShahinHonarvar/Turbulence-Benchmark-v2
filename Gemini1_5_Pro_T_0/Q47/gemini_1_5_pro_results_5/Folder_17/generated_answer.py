def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(22, 96):
        for j in range(i + 51, i + 56):
            if j <= 95:
                substring = text[i:j]
                if len(substring) >= 52 and len(substring) <= 55 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                    palindromes.add(substring)
    return palindromes