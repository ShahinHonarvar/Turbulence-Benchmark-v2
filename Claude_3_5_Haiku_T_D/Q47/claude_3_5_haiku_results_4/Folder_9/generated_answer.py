def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for start in range(301):
        for length in range(50, 61):
            if start + length > 301:
                break
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes