def filter_chars(s):
    result = ''
    for i in range(len(s)):
        if i >= 55 and i < 80:
            if ord('S') < ord(s[i]) < ord('s'):
                result += s[i]
        else:
            result += s[i]
    return result