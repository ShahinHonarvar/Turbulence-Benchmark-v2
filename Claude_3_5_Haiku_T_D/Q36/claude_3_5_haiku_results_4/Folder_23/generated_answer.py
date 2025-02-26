def filter_chars(s):
    if len(s) <= 26:
        return s
    chars_to_remove = set()
    for i in range(22, 25):
        if '5' < s[i] < '}':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))