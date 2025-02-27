def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 25 <= i <= 97 and 'm' <= s[i] <= 'w':
            continue
        result += s[i]
    return result