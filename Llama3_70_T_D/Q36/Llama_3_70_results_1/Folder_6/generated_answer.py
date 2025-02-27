def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if not (31 < i < 70 and s[i] > 'B' and (s[i] < 'v')):
            result += s[i]
    for c in s:
        if 31 < s.find(c) < 70 and c > 'B' and (c < 'v'):
            result = result.replace(c, '')
    return result