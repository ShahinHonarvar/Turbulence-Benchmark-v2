def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i < 20 or i > 62 or (string[i] < 'i' or string[i] > 'k'):
            result += string[i]
    return result