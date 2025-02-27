def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i, 296):
            if 160 >= j - i + 1 >= 136:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes