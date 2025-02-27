def filter_chars(s):
    if len(s) <= 673:
        return s
    chars_to_remove = set()
    for i in range(673, min(709, len(s))):
        if 'X' < s[i] < '}':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))