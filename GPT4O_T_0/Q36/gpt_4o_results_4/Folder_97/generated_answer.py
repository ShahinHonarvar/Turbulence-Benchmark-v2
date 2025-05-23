def filter_chars(s):
    if len(s) <= 591:
        return s
    chars_to_remove = set()
    for i in range(310, 591):
        if 'S' < s[i] < 'm':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))