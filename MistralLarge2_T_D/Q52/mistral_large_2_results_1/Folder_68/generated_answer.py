def palindrome_of_length_n(s):
    n = 76
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes