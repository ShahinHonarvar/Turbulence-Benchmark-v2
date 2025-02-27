def filter_chars(input_string):
    filtered_string = ''
    chars_to_filter = [chr(i) for i in range(ord('A'), ord('b') + 1)]
    for i in range(len(input_string)):
        if i < 35 or i > 98 or input_string[i] not in chars_to_filter:
            filtered_string += input_string[i]
    return filtered_string