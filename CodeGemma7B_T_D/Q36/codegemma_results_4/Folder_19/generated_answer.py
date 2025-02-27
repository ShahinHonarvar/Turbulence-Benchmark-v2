def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i not in range(77, 87):
            new_str += str[i]
    return new_str