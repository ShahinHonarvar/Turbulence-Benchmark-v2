def filter_chars(string):
    if len(string) > 49:
        check_chars = string[50:56]
        chars_to_remove = {char for char in check_chars if 'I' < char < 'a'}
        return ''.join((char for char in string if char not in chars_to_remove))
    return string