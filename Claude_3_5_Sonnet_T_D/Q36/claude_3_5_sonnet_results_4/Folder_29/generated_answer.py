def filter_chars(s):
    chars_to_remove = set()
    for i in range(47, 68):
        if i < len(s) and 'H' < s[i] < 's':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))