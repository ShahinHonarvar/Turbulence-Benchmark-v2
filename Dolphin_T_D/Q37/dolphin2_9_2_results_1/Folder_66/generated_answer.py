def filter_chars(s):
    chars_to_remove = []
    for i in range(27, 86):
        if 'c' <= s[i] <= 'i':
            chars_to_remove.append(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])