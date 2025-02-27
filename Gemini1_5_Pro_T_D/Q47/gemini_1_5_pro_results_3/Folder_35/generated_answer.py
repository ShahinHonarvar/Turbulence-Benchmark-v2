def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(34, 91):
        for j in range(i, 91):
            if 14 <= j - i + 1 <= 39:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes