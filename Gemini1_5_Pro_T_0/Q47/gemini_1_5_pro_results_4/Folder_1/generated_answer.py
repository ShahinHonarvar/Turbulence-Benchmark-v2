def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 90):
        for j in range(i, 90):
            if 40 <= j - i + 1 <= 72:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes