def filter_chars(s):
    if len(s) <= 90:
        return s
    chars_to_remove = set()
    for i in range(91, 97):
        if 'j' < s[i] < 'w':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))