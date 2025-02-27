def filter_chars(s):
    chars_to_filter = [c for c in s if 155 <= s.index(c) <= 403 and ord('(') <= ord(c) <= ord(']')]
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s