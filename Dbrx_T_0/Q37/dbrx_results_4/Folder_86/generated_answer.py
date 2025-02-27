def filter_chars(input_string):
    start_index = 164
    end_index = 706
    chars_to_remove = [c for c in input_string[start_index:end_index + 1] if 'O' <= c <= '}']
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string