def palindromes_of_specific_lengths(s):
    s = s[106:281].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 136, min(i + 152, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes