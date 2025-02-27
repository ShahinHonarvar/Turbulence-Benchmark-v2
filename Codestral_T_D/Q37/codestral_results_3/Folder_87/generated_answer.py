def filter_chars(s):
    for i in range(ord('W'), ord('[') + 1):
        s = s.replace(chr(i), '')
    return s[0:18] + s[18:81].translate(str.maketrans('', '', chr(i))) + s[81:]