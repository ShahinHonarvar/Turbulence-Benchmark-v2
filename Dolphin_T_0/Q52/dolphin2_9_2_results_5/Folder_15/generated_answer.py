def palindrome_of_length_n(s):
    s = s.lower()
    n = 4
    palindrome_set = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            palindrome_set.add(s[i:i + n])
    return palindrome_set