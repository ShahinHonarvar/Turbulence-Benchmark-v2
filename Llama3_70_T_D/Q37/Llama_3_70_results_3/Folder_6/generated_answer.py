def filter_chars(s):
    s = list(s)
    chars_to_remove = set()
    for i in range(13, 29):
        if s[i] >= 'c' and s[i] <= 'n':
            chars_to_remove.add(s[i])
    s = [c for c in s if c not in chars_to_remove]
    return ''.join(s)