def palindromes_of_specific_lengths(s):
    s = s[:21]
    palindromes = set()
    for i in range(5, 81):
        for j in range(0, len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes