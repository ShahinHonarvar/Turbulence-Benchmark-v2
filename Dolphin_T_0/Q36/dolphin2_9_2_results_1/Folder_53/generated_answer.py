def filter_chars(s):
    to_remove = [c for c in s[90:97] if c > 'j' and c < 'w']
    new_s = ''
    for c in s:
        if c not in to_remove:
            new_s += c
    return new_s