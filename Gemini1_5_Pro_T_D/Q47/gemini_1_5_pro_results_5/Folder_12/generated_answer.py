def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(62, 89):
        for j in range(i, 89):
            if 18 <= j - i + 1 <= 21:
                substring = s[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes