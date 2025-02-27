def filter_chars(s):
    return ''.join((i for i in s if i >= 'D' and i <= 'Y' or i < 'A' or i > 'Z' or (i < 'a' or i > 'z')))