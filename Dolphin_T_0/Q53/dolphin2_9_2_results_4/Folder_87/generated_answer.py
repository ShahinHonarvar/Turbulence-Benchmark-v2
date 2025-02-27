def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    for length in range(18, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            if s[i:i + length] == s[i:i + length][::-1]:
                palindrome_set.add(s[i:i + length])
    return palindrome_set