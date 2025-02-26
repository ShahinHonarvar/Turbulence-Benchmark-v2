def filter_chars(s):
    chars_to_remove = set()
    for i in range(44, 59):
        if i < len(s) and '5' < s[i] < 'C':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))