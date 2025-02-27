def filter_chars(my_str):
    new_str = ''
    for char in my_str:
        if 603 <= my_str.index(char) <= 759:
            if 'Q' <= char <= 'h':
                continue
        new_str += char
    return new_str