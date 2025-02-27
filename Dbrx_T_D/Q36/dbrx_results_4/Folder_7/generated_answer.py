def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 502 or i > 945 or (s[i] >= 'W' and s[i] <= 'y'):
            result += s[i]
    return result