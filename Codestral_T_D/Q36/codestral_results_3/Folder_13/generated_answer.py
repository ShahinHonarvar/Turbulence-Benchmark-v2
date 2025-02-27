def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 323 and i < 526:
            if string[i] > ')' and string[i] < 'O':
                continue
        filtered_string += string[i]
    return filtered_string