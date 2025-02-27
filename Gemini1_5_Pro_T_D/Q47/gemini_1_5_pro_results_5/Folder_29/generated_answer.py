def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 95):
        for j in range(i, 95):
            if 18 <= j - i + 1 <= 73:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes