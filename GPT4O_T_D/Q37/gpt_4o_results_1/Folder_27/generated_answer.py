def filter_chars(input_string):
    chars_to_remove = set(input_string[43:81]).intersection(set((chr(i) for i in range(ord('='), ord('E') + 1))))
    return ''.join((char for char in input_string if char not in chars_to_remove))