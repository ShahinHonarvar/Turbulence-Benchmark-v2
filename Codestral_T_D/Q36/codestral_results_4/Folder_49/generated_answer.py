def filter_chars(string):
    chars_to_remove = [chr(i) for i in range(ord('E'), ord('H') + 1)]
    return ''.join([char for char in string if char not in chars_to_remove or string.index(char) < 46 or string.index(char) > 90])