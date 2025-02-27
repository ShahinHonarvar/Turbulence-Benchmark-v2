def filter_chars(s):
    chars_to_remove = [c for c in s[22:86] if c >= '7' and c <= 'e']
    new_s = ''
    for c in s:
        if c not in chars_to_remove:
            new_s += c
    return new_s