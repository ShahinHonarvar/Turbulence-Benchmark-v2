def filter_chars(s):
    to_remove = set()
    for char in s[422:854]:
        if 'D' < char < 'J':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))