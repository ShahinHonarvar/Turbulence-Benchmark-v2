def filter_chars(string):
    start_index = 3
    end_index = 9
    chars_to_remove = [char for char in string[start_index:end_index] if ord('*') < ord(char) < ord('E')]
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string