def filter_chars(s):
    result = ''
    for i in range(0, 31):
        result += s[i]
    for i in range(31, 70):
        if ord('B') < ord(s[i]) < ord('v'):
            s = s.replace(s[i], '')
    for i in range(70, len(s)):
        result += s[i]
    return result