def filter_chars(input_string: str) -> str:
    result = list(input_string)
    for i in range(344, 874):
        char = input_string[i]
        if 'f' < char < '~':
            result.remove(char)
    return ''.join(result)