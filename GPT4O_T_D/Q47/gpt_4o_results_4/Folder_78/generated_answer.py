def palindromes_of_specific_lengths(s):
    s = s[15:73]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = len(s)
    for length in range(19, 56):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes