def filter_chars(s):
    chars_to_remove = set()
    for i in range(11, min(73, len(s))):
        if 'i' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))