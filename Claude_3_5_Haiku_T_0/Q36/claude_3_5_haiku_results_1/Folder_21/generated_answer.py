def filter_chars(s):
    chars_to_remove = set()
    for i in range(220, 403):
        if '*' < s[i] < '7':
            chars_to_remove.add(s[i])
    return ''.join((char for char in s if char not in chars_to_remove))