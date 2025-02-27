def filter_chars(s):
    remove_chars = set()
    for i in range(43, min(81, len(s))):
        if '=' <= s[i] <= 'E':
            remove_chars.add(s[i])
    return ''.join((c for c in s if c not in remove_chars))