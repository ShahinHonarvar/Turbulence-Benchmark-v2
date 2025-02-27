def filter_chars(s):
    chars_to_remove = []
    for i in range(57, 97):
        if '<' <= s[i] <= 'w':
            chars_to_remove.append(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))