def filter_chars(s):
    if len(s) <= 55:
        return s
    chars_to_filter = set()
    for char in s[55:92]:
        if 'J' < char < 'X':
            chars_to_filter.add(char)
    return ''.join((c for c in s if c not in chars_to_filter))