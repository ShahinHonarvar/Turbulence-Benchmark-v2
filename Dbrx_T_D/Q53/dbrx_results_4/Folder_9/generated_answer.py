def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {palindrome for length in range(95, len(s) + 1) for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) == palindrome[::-1] and any((c.isalpha() for c in palindrome))}