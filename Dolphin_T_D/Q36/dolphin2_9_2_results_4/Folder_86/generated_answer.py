def filter_chars(string):
    chars_to_remove = [string[i] for i in range(672, 709) if string[i] > 'X' and string[i] < '}']
    string = ''.join([char for char in string if char not in chars_to_remove])
    return string