def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[18:89]
    palindromes = set()
    for length in range(12, 15):
        for i in range(len(substr) - length + 1):
            substr_str = substr[i:i + length]
            if substr_str.isalpha() and substr_str == substr_str[::-1]:
                palindromes.add(substr_str)
    return palindromes