def filter_chars(string):
    chars_to_remove = [ch for ch in string[18:31] if 'H' < ch < '|']
    for ch in chars_to_remove:
        string = string.replace(ch, '')
    return string