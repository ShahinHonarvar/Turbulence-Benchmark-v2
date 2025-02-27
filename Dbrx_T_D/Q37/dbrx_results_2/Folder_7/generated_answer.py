def filter_chars(input_string):
    start_index = 521
    end_index = 722
    chars_to_remove = []
    for i in range(start_index, end_index + 1):
        if ord('>') <= ord(input_string[i]) <= ord('_'):
            chars_to_remove.append(input_string[i])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string