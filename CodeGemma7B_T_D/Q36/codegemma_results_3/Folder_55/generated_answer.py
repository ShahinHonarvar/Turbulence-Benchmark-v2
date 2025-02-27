def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 3 or i >= 5 or string[i] <= 'Y' or (string[i] >= 's'):
            result += string[i]
    return result