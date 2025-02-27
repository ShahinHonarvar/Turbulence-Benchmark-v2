def filter_chars(s):
    if len(s) <= 90:
        return s
    chars_to_remove = set()
    for ch in s[91:97]:
        if 'j' < ch < 'w':
            chars_to_remove.add(ch)
    return ''.join((ch for ch in s if ch not in chars_to_remove))