def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(106, 281):
        for j in range(i, 281):
            if j - i + 1 >= 136 and j - i + 1 <= 151:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes