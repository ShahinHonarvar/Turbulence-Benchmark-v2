def filter_chars(s):
    result = ''
    for ch in s:
        if 32 <= ord(ch) <= 61 and ch > '3' and (ch < 'D'):
            pass
        else:
            result += ch
    return result