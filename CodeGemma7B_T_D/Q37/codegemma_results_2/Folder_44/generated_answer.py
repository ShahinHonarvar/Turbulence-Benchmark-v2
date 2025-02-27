def filter_chars(s):
    return ''.join([c for c in s if (ord(c) >= ord('+') and ord(c) <= ord('8')) and c not in s[21:44]])