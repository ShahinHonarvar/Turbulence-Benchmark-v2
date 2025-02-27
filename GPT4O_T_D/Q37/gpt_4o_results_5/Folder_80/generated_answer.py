def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 36:
        for i in range(36, min(80, len(s))):
            if 'a' <= s[i] <= 'i':
                chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))