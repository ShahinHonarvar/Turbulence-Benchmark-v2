def filter_chars(s):
    chars_to_remove = set()
    for i in range(603, min(760, len(s))):
        if 'Q' <= s[i] <= 'h':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))