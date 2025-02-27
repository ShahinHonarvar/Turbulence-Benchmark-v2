def filter_chars(string):
    chars_to_remove = [char for char in string if string.index(char) >= 348 and string.index(char) <= 852 and (char >= 'J') and (char <= 'b')]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string