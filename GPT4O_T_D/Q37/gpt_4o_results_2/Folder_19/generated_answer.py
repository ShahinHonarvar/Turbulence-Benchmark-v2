def filter_chars(s):
    chars_to_remove = set()
    for i in range(35, min(90, len(s))):
        if 'E' <= s[i] <= 't':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))