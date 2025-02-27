def insert_after_character(string):
    output = ''
    for ch in string:
        if ch == 'a':
            output += ch + 'n'
        else:
            output += ch
    return output