def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 51 or i > 96 or (input_string[i] < 'X' or input_string[i] > 'p'):
            filtered_string += input_string[i]
    return filtered_string