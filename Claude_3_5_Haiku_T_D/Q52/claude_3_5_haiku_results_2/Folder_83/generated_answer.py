def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 23):
        substr = s[i:i + 24]
        if len(substr) == 24 and substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes