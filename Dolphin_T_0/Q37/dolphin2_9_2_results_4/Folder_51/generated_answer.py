def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[36:41] if char >= 'H' and char <= 'e']
    result_string = input_string
    for char in chars_to_remove:
        result_string = result_string.replace(char, '')
    return result_string