def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 90):
        if s[i:i + 91] == s[i:i + 91][::-1]:
            result.add(s[i:i + 91])
    return result