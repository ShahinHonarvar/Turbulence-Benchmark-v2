def filter_chars(str1):
    str2 = ''.join([x for x in str1 if not (x >= 'l' and x <= 't' and (283 < ord(x) < 484))])
    return str2