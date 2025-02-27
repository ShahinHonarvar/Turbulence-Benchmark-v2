def filter_chars(string):
    filtered_string = []
    for i in range(len(string)):
        if i >= 11 and i <= 72 and (string[i] >= 'i') and (string[i] <= 'v'):
            continue
        filtered_string.append(string[i])
    return ''.join(filtered_string)