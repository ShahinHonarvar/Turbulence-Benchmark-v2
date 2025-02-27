def filter_chars(string):
    filtered_chars = []
    for i in range(len(string)):
        if not (string[i] > 'S' and string[i] < '[' and (i >= 78) and (i < 81)):
            filtered_chars.append(string[i])
    return ''.join(filtered_chars)