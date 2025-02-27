def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    n = 416
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes