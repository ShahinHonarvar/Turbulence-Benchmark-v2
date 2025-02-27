def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for start in range(n - 79):
        substr = s[start:start + 80]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes