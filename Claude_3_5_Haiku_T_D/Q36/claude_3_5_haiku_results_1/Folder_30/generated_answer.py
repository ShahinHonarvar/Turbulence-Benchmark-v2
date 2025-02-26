def filter_chars(s):
    if len(s) <= 46:
        return s
    chars_to_remove = set()
    for i in range(24, 45):
        if '3' < s[i] < 'I':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))