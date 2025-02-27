def filter_chars(string):
    alterd_string = ''
    for i, c in enumerate(string):
        if i < 38 or i > 69 or c < 'H' or (c > 'e'):
            alterd_string += c
    return alterd_string