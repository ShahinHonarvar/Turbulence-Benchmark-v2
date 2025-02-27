def insert_before_character(color):
    x = ''
    for c in color:
        if c == 'A':
            x += 'A' + c
        else:
            x += c
    return x