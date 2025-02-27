def filter_chars(s):
    chars_to_remove = {c for c in map(chr, range(ord(')') + 1, ord('O')))}
    target_chars = s[324:526]
    for char in chars_to_remove:
        if char in target_chars:
            s = s.replace(char, '')
    return s