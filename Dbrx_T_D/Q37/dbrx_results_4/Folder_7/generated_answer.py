def filter_chars(input_string):
    start_index = 520
    end_index = 721
    chars_to_remove = []
    if len(input_string) < end_index:
        return input_string
    for i in range(start_index, end_index + 1):
        char = input_string[i]
        if ord(char) >= ord('>') and ord(char) <= ord('_'):
            chars_to_remove.append(char)
    for char in chars_to_remove:
        while char in input_string:
            input_string = input_string.replace(char, '', 1)
    return input_string