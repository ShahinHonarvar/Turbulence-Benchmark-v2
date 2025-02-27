def filter_chars(input_string: str) -> str:
    for i in range(1, 9):
        char = input_string[i]
        if '8' < char < 'm':
            input_string = input_string.replace(char, '', 1)
    return input_string