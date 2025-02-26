def filter_chars(s):
    chars_to_remove = set()
    for i in range(43, 67):
        if i < len(s) and '6' < s[i] < 'g':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))