def filter_chars(s):
    to_remove = set()
    for char in s[588:648]:
        if ',' < char < 'c':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))