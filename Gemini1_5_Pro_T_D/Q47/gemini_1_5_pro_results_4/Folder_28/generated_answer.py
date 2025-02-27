def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 72):
        for j in range(i, 72):
            substring = s[i:j + 1]
            if 21 <= len(substring) <= 32 and substring.isalpha() and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes