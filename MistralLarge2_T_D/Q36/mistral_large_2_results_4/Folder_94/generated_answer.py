def filter_chars(s):
    chars_to_remove = set()
    for i in range(15, 85):
        if 'I' < s[i] < 'M':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))