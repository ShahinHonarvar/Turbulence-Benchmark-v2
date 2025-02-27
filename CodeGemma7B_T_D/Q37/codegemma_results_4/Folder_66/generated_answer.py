def filter_chars(str1):
    result = ''.join((c for c in str1 if 30 <= ord(c) <= 84 and (ord(c) >= ord('c') and ord(c) <= ord('i'))))
    return result