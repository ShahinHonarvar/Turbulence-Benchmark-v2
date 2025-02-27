def filter_chars(s):
    chars_to_filter = [ch for ch in s[46:68] if ch > 'H' and ch < 's']
    for ch in chars_to_filter:
        s = s.replace(ch, '')
    return s