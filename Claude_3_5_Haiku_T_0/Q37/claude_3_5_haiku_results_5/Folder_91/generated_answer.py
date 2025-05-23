def filter_chars(s):
    chars_to_remove = set()
    for i in range(7, 9):
        if 0 <= i < len(s) and 'B' <= s[i] <= 'H':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))