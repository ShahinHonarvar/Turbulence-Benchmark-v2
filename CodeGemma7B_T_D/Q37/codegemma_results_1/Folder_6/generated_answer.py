def filter_chars(string):
    l = ['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    for i in range(12, 29):
        for c in string[:]:
            if c in l and string.index(c) == i:
                string = string.replace(c, '')
    return string