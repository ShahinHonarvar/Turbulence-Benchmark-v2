def filter_chars(s):
    if len(s) < 89:
        return s
    chars_to_remove = set()
    for i in range(64, 89):
        if '*' < s[i] < 'w':
            chars_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in chars_to_remove))