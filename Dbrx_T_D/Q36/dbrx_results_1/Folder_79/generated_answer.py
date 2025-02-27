def filter_chars(input_string: str) -> str:
    start_index = 11
    end_index = 46
    char_range = range(ord('!') + 1, ord('A'))
    for i, char in enumerate(input_string):
        if start_index <= i < end_index and ord(char) in char_range:
            input_string = input_string.replace(char, '', 1)
    return input_string