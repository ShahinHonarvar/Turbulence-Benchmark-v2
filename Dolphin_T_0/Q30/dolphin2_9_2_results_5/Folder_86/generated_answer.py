def insert_before_character(in_str):
    out_str = ''
    for char in in_str:
        if char == 'O':
            out_str += 'Q' + char
        else:
            out_str += char
    return out_str