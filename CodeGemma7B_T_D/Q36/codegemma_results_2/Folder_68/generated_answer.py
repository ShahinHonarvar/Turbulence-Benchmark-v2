def filter_chars(string):
    if not string:
        return string
    for i in range(1, 9):
        current_char = string[i]
        if current_char > '8' and current_char < 'm':
            while current_char in string:
                string = string.replace(current_char, '', 1)
    return string