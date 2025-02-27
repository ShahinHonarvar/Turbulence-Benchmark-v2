def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 28:
        end_index = min(66, len(s))
        for c in s[28:end_index]:
            if 'O' <= c <= 'd':
                chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))