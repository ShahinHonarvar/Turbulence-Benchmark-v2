def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 42 or i >= 68:
            result += s[i]
    return result