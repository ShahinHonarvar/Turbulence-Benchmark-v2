def filter_chars(s):
    to_remove = set()
    for char in s[220:403]:
        if '*' < char < '7':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))