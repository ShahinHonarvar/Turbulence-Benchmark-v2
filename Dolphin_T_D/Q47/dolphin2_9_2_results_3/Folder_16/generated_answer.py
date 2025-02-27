def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[14:87]
    for i in range(51, 61):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes