def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(18, 66):
        for j in range(i, 66):
            if 23 <= j - i + 1 <= 36:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes