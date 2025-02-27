def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(0, len(s) - 37):
        if s[i:i + 38] == s[i:i + 38][::-1]:
            result.add(s[i:i + 38])
    return result