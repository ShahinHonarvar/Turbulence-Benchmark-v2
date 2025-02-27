def filter_chars(s):
    to_remove = set()
    for char in s[16:85]:
        if 'I' < char < 'M':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))