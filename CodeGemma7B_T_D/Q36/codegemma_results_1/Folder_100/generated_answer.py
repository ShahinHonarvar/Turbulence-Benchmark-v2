def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 43 or i >= 69 or string[i] <= 'B' or (string[i] >= 'r'):
            result += string[i]
    return result