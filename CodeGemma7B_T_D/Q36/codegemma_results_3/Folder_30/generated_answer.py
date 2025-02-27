def filter_chars(string):
    new_string = ''.join([char for i, char in enumerate(list(string)) if i < 23 or i > 45])
    return new_string