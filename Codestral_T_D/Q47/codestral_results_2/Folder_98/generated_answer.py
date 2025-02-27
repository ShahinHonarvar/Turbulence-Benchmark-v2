def palindromes_of_specific_lengths(s):
    s = s[:21]
    s = s.lower()
    palindromes = set()
    for length in range(5, 81):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes