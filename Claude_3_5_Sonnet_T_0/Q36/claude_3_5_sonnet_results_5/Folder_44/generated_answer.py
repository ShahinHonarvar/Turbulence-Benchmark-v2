def filter_chars(s):
    chars_to_remove = set()
    for i in range(19, 64):
        if i < len(s) and '3' < s[i] < 'B':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))