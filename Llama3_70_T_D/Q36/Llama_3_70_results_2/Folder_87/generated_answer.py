def filter_chars(s):
    result = ''
    for c in s:
        if (ord(c) < 32 or ord(c) >= 61) or not (c > '3' and c < 'D'):
            result += c
    return result