def insert_before_character(Str):
    output_str = ''
    for i in range(len(Str)):
        if Str[i] == 'N':
            output_str = output_str + 'z'
        output_str = output_str + Str[i]
    return output_str