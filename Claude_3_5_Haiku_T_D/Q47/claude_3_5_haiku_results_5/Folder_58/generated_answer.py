def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(109, 127):
        for start in range(125, 284 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes