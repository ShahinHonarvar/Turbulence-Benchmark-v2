def filter_chars(string):
    chars_to_remove = [string[i] for i in range(19, 33) if 'f' <= string[i] <= 'o']
    return ''.join([char for char in string if char not in chars_to_remove])