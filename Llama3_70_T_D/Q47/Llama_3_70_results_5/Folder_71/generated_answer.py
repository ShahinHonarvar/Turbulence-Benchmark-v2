def palindromes_of_specific_lengths(s):
    s = s[18:66].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(23, 37):
            substring = s[i:i + j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes