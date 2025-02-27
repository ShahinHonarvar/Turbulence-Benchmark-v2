def palindrome_of_length_n(s):
    s = s.lower()
    n = 91
    palindrome_set = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindrome_set.add(substr)
    return palindrome_set