def filter_chars(s):
    remove_chars = set()
    for i in range(35, 99):
        if 'A' <= s[i] <= 'b':
            remove_chars.add(s[i])
    return ''.join((c for c in s if c not in remove_chars))