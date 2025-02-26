def filter_chars(input_string):
    result = list(input_string)
    for i in range(44, 83):
        if ':' < input_string[i] < 'Q':
            char_to_remove = input_string[i]
            result = [char for char in result if char != char_to_remove]
    return ''.join(result)