def filter_chars(str):
    result = str[:24]
    for i in range(24, 37):
        if str[i] > 'A' and str[i] < 'h':
            for j in range(i, len(str)):
                if str[j] == str[i]:
                    str[j] = ''
    return result + str[37:]