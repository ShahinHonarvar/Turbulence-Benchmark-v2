def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i < 1 or i > 7 or (ord(s[i]) >= ord('L') and ord(s[i]) <= ord('a')):
            result += s[i]
    return result