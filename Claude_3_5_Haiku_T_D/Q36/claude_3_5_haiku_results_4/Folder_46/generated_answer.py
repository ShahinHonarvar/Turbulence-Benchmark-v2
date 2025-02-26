def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if 19 < i < 69 and '<' < s[i] < 'C':
            result = s.replace(s[i], '')
            s = result
    return s