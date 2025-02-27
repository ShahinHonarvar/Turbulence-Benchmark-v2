def insert_after_character(in_string):
    out_string = ''
    for char in in_string:
        out_string += char
        if char == 'x':
            out_string += 'N'
    return out_string