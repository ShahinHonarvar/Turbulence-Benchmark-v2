def filter_chars(s):
    remove_chars = set()
    for char in s[310:591]:
        if 'S' < char < 'm':
            remove_chars.add(char)
    return ''.join((char for char in s if char not in remove_chars))