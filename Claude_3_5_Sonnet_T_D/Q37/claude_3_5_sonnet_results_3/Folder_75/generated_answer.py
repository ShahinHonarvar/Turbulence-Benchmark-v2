def filter_chars(s):
    chars_to_remove = set()
    for i in range(34, 68):
        if i < len(s) and 'W' <= s[i] <= 'x':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))