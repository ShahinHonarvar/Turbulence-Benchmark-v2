def filter_chars(input_string: str) -> str:
    filtered_string = ''
    for i in range(len(input_string)):
        if i < 21 or i > 43 or (input_string[i] < '+' or input_string[i] > '8'):
            filtered_string += input_string[i]
    return filtered_string