def palindrome_of_length_n(s):
    n = 94
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes