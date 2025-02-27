def filter_chars(input_str):
    filtered_str = input_str[:42]
    for char in input_str[42:93]:
        if char >= '/' and char <= 'a':
            input_str = input_str.replace(char, '', 1)
    filtered_str += input_str[93:]
    return filtered_str