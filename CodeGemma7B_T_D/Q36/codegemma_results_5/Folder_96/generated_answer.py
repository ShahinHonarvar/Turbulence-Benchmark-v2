def filter_chars(str):
    str = list(str)
    for i in range(38, 81):
        str = [symbol for symbol in str if symbol != str[i]]
    return ''.join(str)