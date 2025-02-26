def remove_repeat_chars(string):
    segment = string[356:988]
    repeat_chars = set((char for char in segment if segment.count(char) > 1))
    return ''.join((char for char in string if char not in repeat_chars))