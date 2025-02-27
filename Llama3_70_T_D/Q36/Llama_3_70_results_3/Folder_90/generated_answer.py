def filter_chars(s):
    chars_to_remove = set()
    for i in range(344, 874):
        if s[i] > 'f' and s[i] < '~':
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])