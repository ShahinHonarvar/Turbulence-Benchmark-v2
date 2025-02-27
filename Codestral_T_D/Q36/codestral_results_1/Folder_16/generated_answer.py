def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('M') + 1, ord('_'))]
    return ''.join((char for char in s if char not in chars_to_remove[331:713]))