def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i > 1 and i < 7 and (string[i] > '3') and (string[i] < '^'):
            continue
        else:
            new_string += string[i]
    return new_string