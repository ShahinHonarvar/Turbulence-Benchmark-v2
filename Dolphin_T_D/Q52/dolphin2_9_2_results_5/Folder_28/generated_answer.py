def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 42):
        if s[i:i + 43] == s[i:i + 43][::-1]:
            result.add(s[i:i + 43])
    return result