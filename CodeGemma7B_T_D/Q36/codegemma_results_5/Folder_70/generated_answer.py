def filter_chars(string):
    new_str = ''
    for i in range(len(string)):
        if i < 170 or i > 195:
            new_str += string[i]
    return new_str