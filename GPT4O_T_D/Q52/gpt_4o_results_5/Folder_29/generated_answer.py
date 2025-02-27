def palindrome_of_length_n(s):
    palindromes = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n - 18):
        substr = s[i:i + 19]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes