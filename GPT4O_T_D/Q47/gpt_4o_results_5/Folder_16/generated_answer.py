def palindromes_of_specific_lengths(s):
    s = s[15:87]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(51, 61):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes