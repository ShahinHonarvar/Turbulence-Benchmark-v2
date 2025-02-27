def filter_chars(s):
    if len(s) <= 21:
        return s
    chars_to_remove = set()
    for i in range(22, min(25, len(s))):
        if '5' < s[i] < '}':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))