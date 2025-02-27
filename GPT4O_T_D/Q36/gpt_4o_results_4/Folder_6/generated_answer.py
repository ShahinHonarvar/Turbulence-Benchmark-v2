def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 31:
        for i in range(32, min(70, len(s))):
            if 'B' < s[i] < 'v':
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))