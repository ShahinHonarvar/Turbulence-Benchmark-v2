def filter_chars(s):
    chars_to_remove = set()
    for i in range(min(83, len(s)), min(99, len(s)) + 1):
        if '*' <= s[i] <= 'j':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))