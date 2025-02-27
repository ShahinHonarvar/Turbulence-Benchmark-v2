def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 373:
        end_range = min(len(s), 902)
        for char in s[373:end_range]:
            if 'T' <= char <= 'h':
                chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))