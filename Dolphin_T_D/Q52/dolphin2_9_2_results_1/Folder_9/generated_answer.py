def palindrome_of_length_n(s):
    s = s.lower()
    length = 72
    palindrome_set = set()
    for i in range(len(s) - length + 1):
        if s[i:i + length] == s[i:i + length][::-1]:
            palindrome_set.add(s[i:i + length])
    return palindrome_set