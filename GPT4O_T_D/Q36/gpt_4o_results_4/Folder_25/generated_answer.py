def filter_chars(s):
    chars_to_remove = set()
    for ch in s[25:37]:
        if 'A' < ch < 'h':
            chars_to_remove.add(ch)
    return ''.join((ch for ch in s if ch not in chars_to_remove))