def filter_chars(s):
    chars_to_remove = set()
    for i in range(26, min(65, len(s))):
        if 'V' <= s[i] <= 'o':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))