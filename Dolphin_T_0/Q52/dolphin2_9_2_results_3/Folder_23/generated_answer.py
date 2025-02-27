def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = 69
    n = len(s)
    palindromes = set()
    for i in range(n - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes