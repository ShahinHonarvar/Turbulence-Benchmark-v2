def filter_chars(input_string):
    chars_to_remove = ''.join([chr(i) for i in range(ord('.'), ord('b') + 1) if 72 <= i % 100 <= 94])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string