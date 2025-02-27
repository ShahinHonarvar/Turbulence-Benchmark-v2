def filter_chars(string):
    chars_to_remove = set()
    for char in string[22:86]:
        if '7' <= char <= 'e':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string