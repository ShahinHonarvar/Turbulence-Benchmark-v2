def palindromes_of_specific_lengths(s):
    s = s[:21]
    s = s.lower()
    palindromes = set()
    for i in range(5, 81):
        for j in range(len(s) - i + 1):
            substring = s[j:j + i]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes