def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 46 or i > 85:
            new_str += str[i]
        elif str[i] != '-':
            new_str += str[i]
    return new_str