def filter_chars(input_string: str) -> str:
    for i in range(min(len(input_string), 2), min(len(input_string), 6) + 1):
        if '?' <= input_string[i] <= 'f':
            input_string = input_string[:i] + input_string[i + 1:]
    return input_string