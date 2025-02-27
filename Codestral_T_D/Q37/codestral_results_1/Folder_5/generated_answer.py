def filter_chars(string):
    new_string = ''
    for i in range(len(string)):
        if i >= 24 and i <= 82 and ('5' <= string[i] <= '<'):
            continue
        new_string += string[i]
    return new_string