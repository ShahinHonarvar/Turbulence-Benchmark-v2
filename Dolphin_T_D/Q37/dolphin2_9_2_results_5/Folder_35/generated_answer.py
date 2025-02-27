def filter_chars(s):
    to_filter = [ch for i, ch in enumerate(s) if 155 <= i <= 403 and ord('(') <= ord(ch) <= ord(']')]
    for ch in to_filter:
        s = s.replace(ch, '')
    return s