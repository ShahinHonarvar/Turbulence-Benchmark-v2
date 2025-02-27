def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(29, 97):
        for j in range(i, 97):
            if 12 <= j - i + 1 <= 18:
                substring = s[i:j + 1]
                if substring.isalpha() and substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes