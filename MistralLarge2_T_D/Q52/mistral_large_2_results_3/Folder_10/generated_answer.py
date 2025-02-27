def palindrome_of_length_n(s):
    n = 54
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = ''.join(filter(str.isalpha, s[i:i + n]))
        if len(substr) == n and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes