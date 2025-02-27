def filter_chars(string):
    for i in range(502, 946):
        for j in range(i, len(string)):
            if string[i] == string[j] and string[i] > 'W' and (string[i] < 'y'):
                string = string[:j] + string[j + 1:]
    return string