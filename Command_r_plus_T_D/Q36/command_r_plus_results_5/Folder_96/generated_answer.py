def filter_chars(input_string: str) -> str:
    filtered_string = input_string[:38]
    for char in input_string[38:81]:
        if '.' < char < '^':
            filtered_string += input_string[input_string.index(char):].replace(char, '')
            break
    filtered_string += input_string[81:]
    return filtered_string