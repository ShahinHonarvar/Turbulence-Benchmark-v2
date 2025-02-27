def filter_chars(string):
    chars_to_remove = [chr(c) for c in range(ord('5') + 1, ord('C')) if string[43:59].count(chr(c)) > 0]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string