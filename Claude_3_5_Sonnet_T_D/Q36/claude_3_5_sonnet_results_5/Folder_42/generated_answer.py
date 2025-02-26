def filter_chars(s):
    chars_to_remove = set()
    for i in range(43, 68):
        if i < len(s) and 't' < s[i] < 'x':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))