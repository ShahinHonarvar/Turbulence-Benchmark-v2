def filter_chars(s):
    remove_chars = set()
    for char in s[422:854]:
        if 'D' < char < 'J':
            remove_chars.add(char)
    return ''.join((char for char in s if char not in remove_chars))