def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 44 or i > 59 or (not '/' < s[i] < '6'):
            result += s[i]
    return result