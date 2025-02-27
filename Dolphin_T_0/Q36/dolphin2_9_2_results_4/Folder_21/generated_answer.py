def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 219 or i >= 403:
            result += s[i]
        elif not (s[i] > '*' and s[i] < '7'):
            result += s[i]
    return result