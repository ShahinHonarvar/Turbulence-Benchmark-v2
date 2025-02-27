def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i in range(12, 89):
            if not '&' <= string[i] <= 'v':
                result += string[i]
        else:
            result += string[i]
    return result