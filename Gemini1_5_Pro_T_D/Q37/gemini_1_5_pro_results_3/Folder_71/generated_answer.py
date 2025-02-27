def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if not (i in range(32, 47) and ord(c) >= ord('0') and (ord(c) <= ord('k'))):
            result += c
    return result