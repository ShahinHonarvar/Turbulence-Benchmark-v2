def filter_chars(string):
    new_string = string
    for i in range(len(string)):
        if i > 1 and i < 7 and (string[i] > '3') and (string[i] < '^'):
            new_string = new_string.replace(string[i], '')
    return new_string