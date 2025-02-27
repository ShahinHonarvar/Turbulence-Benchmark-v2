def filter_chars(input_str):
    filtered_str = ''
    for i in range(81, 86):
        char = input_str[i]
        if char > '!' and char < 's':
            filtered_str += char
    for char in input_str:
        if char not in filtered_str:
            filtered_str += char
    return filtered_str