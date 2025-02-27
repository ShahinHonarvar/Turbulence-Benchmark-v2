def filter_chars(str):
    filtered_str = ''
    for i in range(54, 92):
        if str[i] > 'J' and str[i] < 'X':
            continue
        filtered_str += str[i]
    return filtered_str