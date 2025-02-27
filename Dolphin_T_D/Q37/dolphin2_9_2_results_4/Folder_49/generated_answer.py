def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i >= 42 and i <= 97 and (string[i] >= '*') and (string[i] <= 'b'):
            continue
        else:
            result += string[i]
    return result