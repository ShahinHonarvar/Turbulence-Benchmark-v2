def filter_chars(input_string: str) -> str:
    result = []
    for index, char in enumerate(input_string):
        if 83 <= index <= 99 and '*' <= char <= 'j':
            continue
        result.append(char)
    return ''.join(result)