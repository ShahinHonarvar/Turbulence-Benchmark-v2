def filter_chars(s):
    result = ('',)
    for i in range(len(s)):
        if i >= 54 and i <= 62 and (s[i] >= ')') and (s[i] <= '9'):
            continue
        result += s[i]
    return ''.join(result)