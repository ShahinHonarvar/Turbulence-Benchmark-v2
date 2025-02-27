def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 86 and i <= 92 and (ord(string[i]) >= ord('!')) and (ord(string[i]) <= ord('s')):
            continue
        filtered_string += string[i]
    return filtered_string