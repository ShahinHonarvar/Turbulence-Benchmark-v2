def filter_chars(s):
    chars = [ch for ch in s[18:63] if ch > '3' and ch < 'B']
    for ch in chars:
        s = s.replace(ch, '')
    return s