def filter_chars(s):
    if len(s) <= 9:
        return s
    chars_to_remove = set()
    for i in range(5, 8):
        if '1' < s[i] < 'J':
            chars_to_remove.add(s[i])
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result