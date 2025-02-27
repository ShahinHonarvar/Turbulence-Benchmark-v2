def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 29 or i > 97 or (input_string[i] < '-' and input_string[i] > 'n'):
            filtered_string += input_string[i]
    return filtered_string