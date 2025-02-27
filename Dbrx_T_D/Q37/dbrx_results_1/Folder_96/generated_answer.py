def filter_chars(input_string):
    start_index = 86
    end_index = 92
    filtered_chars = input_string[:start_index]
    for char in input_string[start_index:end_index + 1]:
        if not '!' <= char <= 's':
            filtered_chars += char
    filtered_chars += input_string[end_index + 1:]
    return filtered_chars