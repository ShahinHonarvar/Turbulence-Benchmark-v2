def filter_chars(input_string):
    chars_to_remove = [chr(i) for i in range(ord('='), ord('E') + 1)]
    result = ''.join([char for char in input_string if char not in chars_to_remove or (input_string.index(char) < 43 or input_string.index(char) > 80)])
    return result