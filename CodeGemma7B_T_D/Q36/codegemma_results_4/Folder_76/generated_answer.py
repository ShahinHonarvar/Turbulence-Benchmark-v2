def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 669 or i >= 888:
            new_str += str[i]
    for i in range(669, 888):
        while str[i] in new_str:
            new_str = new_str.replace(str[i], '')
    return new_str