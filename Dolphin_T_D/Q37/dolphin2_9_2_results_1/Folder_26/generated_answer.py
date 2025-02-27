def filter_chars(string):
    chars_to_remove = [string[i] for i in range(20, 63) if 'i' <= string[i] <= 'k']
    return ''.join([char for char in string if char not in chars_to_remove])