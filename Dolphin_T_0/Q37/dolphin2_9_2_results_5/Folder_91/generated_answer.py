def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if 7 <= i <= 8 and 'B' <= string[i] <= 'H':
            continue
        else:
            result += string[i]
    return result