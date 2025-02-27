def filter_chars(input_string: str) -> str:
    result = []
    for i, char in enumerate(input_string):
        if 24 < i < 37 and 'A' < char < 'h':
            continue
        result.append(char)
    return ''.join(result)