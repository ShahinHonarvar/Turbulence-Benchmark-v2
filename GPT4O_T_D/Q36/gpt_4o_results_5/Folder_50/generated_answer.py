def filter_chars(s):
    if len(s) <= 62:
        return s
    to_remove = set()
    for char in s[62:88]:
        if '%' < char < 'q':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))