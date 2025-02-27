def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(14, 91):
        for j in range(i, 91):
            if 55 <= j - i + 1 <= 71:
                substring = text[i:j + 1]
                if all((c.isalpha() for c in substring)) and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes