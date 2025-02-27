def filter_chars(s):
    chars_to_filter = [c for i, c in enumerate(s) if 20 <= i <= 62 and 'i' <= c <= 'k']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s