def filter_chars(input_string):
    if len(input_string) < 42:
        return input_string
    chars_to_remove = set()
    for char in input_string[42:98]:
        if '*' <= char <= 'b':
            chars_to_remove.add(char)
    return ''.join((char for char in input_string if char not in chars_to_remove))