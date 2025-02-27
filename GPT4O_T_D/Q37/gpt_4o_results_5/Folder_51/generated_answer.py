def filter_chars(s):
    if len(s) < 41:
        return s
    remove_chars = set()
    for i in range(36, 41):
        if 'H' <= s[i] <= 'e':
            remove_chars.add(s[i])
    return ''.join((c for c in s if c not in remove_chars))