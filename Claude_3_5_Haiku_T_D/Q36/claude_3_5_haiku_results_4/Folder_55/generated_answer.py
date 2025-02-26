def filter_chars(s):
    if len(s) <= 4:
        return s
    chars_to_remove = set()
    for i in range(4, len(s) - 1):
        if 'Y' < s[i] < 's':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))