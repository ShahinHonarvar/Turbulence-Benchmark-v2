def filter_chars(s):
    chars_to_remove = []
    for i in range(22, 86):
        if '7' <= s[i] <= 'e':
            chars_to_remove.append(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])