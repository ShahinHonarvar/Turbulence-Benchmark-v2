def remove_repeat_chars(input_string):
    output_string = ''
    for i in range(10):
        if input_string[i] not in output_string:
            output_string += input_string[i]
    return output_string