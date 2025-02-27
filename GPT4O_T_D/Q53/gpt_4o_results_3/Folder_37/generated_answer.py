def palindrome_of_length_at_least_n(s):
    n = 67
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + n, len(s) + 1):
            substr = s[start:end]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes