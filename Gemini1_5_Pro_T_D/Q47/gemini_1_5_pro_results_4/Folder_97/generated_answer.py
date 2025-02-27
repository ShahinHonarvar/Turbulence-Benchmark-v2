def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(28, 95):
        for j in range(i, 95):
            if 38 <= j - i + 1 <= 49:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes