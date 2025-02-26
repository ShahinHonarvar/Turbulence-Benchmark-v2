def filter_chars(input_string):
    chars_to_remove = set((char for i, char in enumerate(input_string) if 10 <= i <= 52 and '@' <= char <= 'T'))
    return ''.join((char for char in input_string if char not in chars_to_remove))