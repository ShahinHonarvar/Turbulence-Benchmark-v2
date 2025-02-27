def filter_chars(s):
    to_remove = set()
    for char in s[37:57]:
        if '6' <= char <= '_':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))