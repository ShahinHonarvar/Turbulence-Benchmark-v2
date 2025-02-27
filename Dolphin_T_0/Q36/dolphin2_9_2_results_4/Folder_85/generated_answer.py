def filter_chars(string):
    chars_to_remove = [c for c in string[55:80] if c > 'S' and c < 's']
    for c in chars_to_remove:
        string = string.replace(c, '')
    return string