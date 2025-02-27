def palindromes_of_specific_lengths(s):
    s = s[10:75]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(6, 9):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes