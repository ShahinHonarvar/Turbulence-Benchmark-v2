def filter_chars(s):
    chars_to_remove = set()
    for i in range(20, min(63, len(s))):
        if 'i' <= s[i] <= 'k':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))