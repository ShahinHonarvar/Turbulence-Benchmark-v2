def filter_chars(s):
    chars_to_remove = set()
    for i in range(32, 47):
        if '0' <= s[i] <= 'k':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))