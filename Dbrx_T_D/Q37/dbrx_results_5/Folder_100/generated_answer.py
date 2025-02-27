def filter_chars(input_string):
    chars_to_filter = set(input_string[88:91])
    filtered_chars = chars_to_filter & set('JKLMNOPQR')
    output_string = ''.join([char for char in input_string if char not in filtered_chars])
    return output_string