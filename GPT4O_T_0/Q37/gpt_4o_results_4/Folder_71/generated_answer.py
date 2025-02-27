def filter_chars(s):
    chars_to_remove = set()
    for i in range(32, min(47, len(s))):
        if '0' <= s[i] <= 'k':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))