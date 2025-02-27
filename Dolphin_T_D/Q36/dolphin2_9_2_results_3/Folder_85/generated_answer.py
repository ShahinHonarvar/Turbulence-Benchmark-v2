def filter_chars(s):
    chars_to_filter = [ch for ch in s[55:80] if ch > 'S' and ch < 's']
    for ch in chars_to_filter:
        s = s.replace(ch, '')
    return s