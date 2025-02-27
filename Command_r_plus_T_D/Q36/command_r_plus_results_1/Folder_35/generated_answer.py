def filter_chars(input_string: str) -> str:
    result = []
    delete_chars = []
    for char in input_string[163:659]:
        if '(' < char < ']':
            delete_chars.append(char)
        else:
            result.append(char)
    for char in input_string[:163]:
        if char not in delete_chars:
            result.append(char)
    for char in input_string[659:]:
        if char not in delete_chars:
            result.append(char)
    return ''.join(result)