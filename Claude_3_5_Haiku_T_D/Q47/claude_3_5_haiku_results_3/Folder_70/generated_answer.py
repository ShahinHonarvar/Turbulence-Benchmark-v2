def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[10:71]
    palindromes = set()
    for length in range(24, 53):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes