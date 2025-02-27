def filter_chars(input_string):
    chars_to_remove = [chr(i) for i in range(ord('_'), ord('o') + 1)]
    result = ''.join([char for char in input_string if char not in chars_to_remove])
    return result