def insert_after_character(input_string):
    output_string = input_string[:]
    i = 0
    while i < len(output_string) - 1:
        if output_string[i] == 'o':
            output_string = output_string[:i + 1] + 'a' + output_string[i + 1:]
            i += 1
        i += 1
    return output_string