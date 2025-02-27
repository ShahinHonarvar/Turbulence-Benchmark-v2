def filter_chars(str):
    temp_str = ''
    for i in range(len(str)):
        if i >= 54 and i <= 92:
            if str[i] > 'J' and str[i] < 'X':
                continue
        temp_str += str[i]
    return temp_str