def palindromes_of_specific_lengths(s):
    s = s[:31]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes