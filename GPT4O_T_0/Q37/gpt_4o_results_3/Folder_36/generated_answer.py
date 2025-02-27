def filter_chars(s):
    chars_to_remove = set()
    for i in range(259, min(503, len(s))):
        if ',' <= s[i] <= '3':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))