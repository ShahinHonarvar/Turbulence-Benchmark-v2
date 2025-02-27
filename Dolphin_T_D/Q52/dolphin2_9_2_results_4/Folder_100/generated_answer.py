def palindrome_of_length_n(s):
    n = 91
    result = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            result.add(s[i:i + n])
    return result