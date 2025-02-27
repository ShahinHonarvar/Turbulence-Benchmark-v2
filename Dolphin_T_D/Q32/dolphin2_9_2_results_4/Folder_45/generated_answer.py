def insert_after_character(in_String):
    out_String = ''
    for i in range(len(in_String)):
        out_String += in_String[i]
        if in_String[i] == 'O':
            out_String += 'O'
    return out_String