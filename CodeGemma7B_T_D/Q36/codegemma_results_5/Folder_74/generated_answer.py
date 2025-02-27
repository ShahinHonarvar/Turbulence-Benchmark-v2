def filter_chars(str):
    i = 32
    while i < 36:
        index = str.find(chr(i))
        if index != -1:
            str = str[:index] + str[index + 1:]
        i += 1
    return str