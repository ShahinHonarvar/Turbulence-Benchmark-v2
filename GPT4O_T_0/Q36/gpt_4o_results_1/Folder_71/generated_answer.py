def filter_chars(s):
    if len(s) <= 82:
        return s
    chars_to_remove = set()
    for i in range(83, 89):
        if '*' < s[i] < '[':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))