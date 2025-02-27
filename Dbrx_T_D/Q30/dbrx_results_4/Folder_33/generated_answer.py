def insert_before_character(input_string: str) -> str:
    n_char = 'n'
    a_char = 'a'
    output_list = []
    for char in input_string:
        if char == a_char:
            output_list.append(n_char)
        output_list.append(char)
    return ''.join(output_list)