def filter_chars(string):
    for i in range(77, 87):
        char = string[i]
        if char > ';' and char < 'r':
            string = ''.join((c for c in string if c != char))
    return string