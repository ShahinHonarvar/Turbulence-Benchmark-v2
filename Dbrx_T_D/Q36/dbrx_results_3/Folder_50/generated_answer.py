def filter_chars(input_string):
    start_index = 61
    end_index = 88
    chars_to_remove = set(input_string[start_index:end_index])
    chars_to_remove = {char for char in chars_to_remove if ord('%') < ord(char) < ord('q')}
    result = ''.join((char for char in input_string if char not in chars_to_remove))
    return result