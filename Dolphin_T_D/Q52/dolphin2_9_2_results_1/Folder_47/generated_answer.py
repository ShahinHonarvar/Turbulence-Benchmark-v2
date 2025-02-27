def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 33):
        if s[i:i + 35] == s[i:i + 35][::-1] and s[i:i + 35] != ' ' * 35:
            result.add(s[i:i + 35])
    return result