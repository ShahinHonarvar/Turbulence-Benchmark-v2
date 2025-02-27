def filter_chars(input_string):
    start_index = 164
    end_index = 706
    filtered_string = ''
    chars_to_remove = [chr(i) for i in range(ord('O'), ord('}') + 1)]
    for i in range(len(input_string)):
        if i < start_index or i > end_index or input_string[i] not in chars_to_remove:
            filtered_string += input_string[i]
    return filtered_string