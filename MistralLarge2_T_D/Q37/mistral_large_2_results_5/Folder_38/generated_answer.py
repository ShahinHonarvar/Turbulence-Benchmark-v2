def filter_chars(string):
    chars_to_remove = set()
    for i in range(24, 80):
        if 'a' <= string[i] <= 'f':
            chars_to_remove.add(string[i])
    return ''.join((c for c in string if c not in chars_to_remove))