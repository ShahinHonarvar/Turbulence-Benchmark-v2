def filter_chars(string):
    filtered_string = []
    for i in range(len(string)):
        if string[i] >= 'S' and string[i] <= '{':
            if i >= 19 and i <= 33:
                continue
        filtered_string.append(string[i])
    return ''.join(filtered_string)