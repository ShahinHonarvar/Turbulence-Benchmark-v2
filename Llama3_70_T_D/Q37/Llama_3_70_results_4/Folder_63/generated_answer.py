def filter_chars(s):
    remove_chars = set()
    for char in s[42:93]:
        if '/' <= char <= 'a':
            remove_chars.add(char)
    return ''.join([c for c in s if c not in remove_chars])