def filter_chars(s):
    chars_to_remove = set()
    for i in range(24, 80):
        if 'a' <= s[i] <= 'f':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))