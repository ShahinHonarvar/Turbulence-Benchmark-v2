def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        if s[i:i + 38] == s[i:i + 38][::-1]:
            result.add(s[i:i + 38])
    return result