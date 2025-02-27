def filter_chars(s):
    chars_to_check = ''.join((ch for i, ch in enumerate(s) if 42 <= i <= 67))
    for ch in chars_to_check:
        if 't' < ch < 'x':
            s = ''.join((ch2 for ch2 in s if ch2 != ch))
    return s