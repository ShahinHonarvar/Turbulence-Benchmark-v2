def filter_chars(s):
    to_remove = set()
    for char in s[220:403]:
        if '*' < char < '7':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))