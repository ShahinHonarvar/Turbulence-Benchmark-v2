def filter_chars(s):
    chars_to_remove = set()
    for i in range(44, 59):
        if s[i] > '/' and s[i] < '6':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))