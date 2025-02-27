def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 13 and i < 40:
            if ord(string[i]) > ord(':') and ord(string[i]) < ord('C'):
                filtered_string = filtered_string + string[i]
    return filtered_string