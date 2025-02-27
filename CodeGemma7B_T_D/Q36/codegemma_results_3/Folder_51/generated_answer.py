def filter_chars(string):
    filtered_str = ''
    for i in range(len(string)):
        if i < 58 or i >= 81 or (string[i] > '5' and string[i] < '>'):
            filtered_str += string[i]
    return filtered_str