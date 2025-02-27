def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i in range(19, 33) and s[i] in 'f' <= s[i] <= 'o':
            continue
        result += s[i]
    return result