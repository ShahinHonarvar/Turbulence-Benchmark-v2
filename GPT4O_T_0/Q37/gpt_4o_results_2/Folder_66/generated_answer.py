def filter_chars(s):
    chars_to_remove = set()
    for i in range(27, min(86, len(s))):
        if 'c' <= s[i] <= 'i':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))