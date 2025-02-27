def palindromes_of_specific_lengths(s):
    substring = s[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(0, len(substring) - length + 1):
            pi = substring[i:i + length]
            if pi == pi[::-1] and pi.isalpha():
                palindromes.add(pi)
    return palindromes