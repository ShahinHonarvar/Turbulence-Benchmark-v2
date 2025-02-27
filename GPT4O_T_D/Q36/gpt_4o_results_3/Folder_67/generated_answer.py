def filter_chars(s):
    if len(s) <= 19:
        return s
    chars_to_remove = set()
    for ch in s[19:31]:
        if 'H' < ch < '|':
            chars_to_remove.add(ch)
    return ''.join((ch for ch in s if ch not in chars_to_remove))