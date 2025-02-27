def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 275):
        if s[i:i + 276] == s[i:i + 276][::-1]:
            result.add(s[i:i + 276])
    return result