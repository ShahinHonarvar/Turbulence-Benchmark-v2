def filter_chars(s):
    start, end = (3, 9)
    chars_to_filter = [c for c in s[start:end] if '*' < c < 'E']
    for c in chars_to_filter:
        s = s.replace(c, '', end - start)
    return s