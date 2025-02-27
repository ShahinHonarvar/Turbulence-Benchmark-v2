def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 42 or i >= 78:
            new_str += str[i]
        elif str[i] > '!' and str[i] < '?':
            new_str += ''
    return new_str