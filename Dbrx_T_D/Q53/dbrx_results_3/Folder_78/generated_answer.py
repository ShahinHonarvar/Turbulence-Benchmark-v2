def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {palindrome for length in range(12, 0, -1) for start in range(len(s) - length + 1) for palindrome in [s[start:start + length]] if palindrome == palindrome[::-1] and len(palindrome) >= 96}