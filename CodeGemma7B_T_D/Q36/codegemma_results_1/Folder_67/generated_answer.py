def filter_chars(string):
    for i in range(18, 31):
        current_char = string[i]
        if current_char > 'H' and current_char < '|':
            while current_char in string:
                string = string.replace(current_char, '')
    return string