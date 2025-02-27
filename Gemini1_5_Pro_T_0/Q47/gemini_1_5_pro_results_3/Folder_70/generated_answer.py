def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(10, 71):
        for j in range(i, 71):
            if 24 <= j - i + 1 <= 52:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes