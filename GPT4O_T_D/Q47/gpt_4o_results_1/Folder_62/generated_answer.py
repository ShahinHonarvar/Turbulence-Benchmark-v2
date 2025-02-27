def palindromes_of_specific_lengths(s):
    s = s[26:88]
    s = ''.join(filter(str.isalpha, s)).lower()
    lengths = range(52, 57)
    palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes