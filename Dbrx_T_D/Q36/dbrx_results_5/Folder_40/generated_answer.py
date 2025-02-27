def filter_chars(input_string: str) -> str:
    for i in range(1, 8):
        if input_string[i] > '-' and input_string[i] < 'L':
            input_string = input_string.replace(input_string[i], '')
    return input_string