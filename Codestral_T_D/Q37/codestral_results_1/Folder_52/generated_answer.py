def filter_chars(string):
    result = ''
    for i in range(len(string)):
        if i >= 54 and i <= 83 and ('j' <= string[i] <= 'v'):
            continue
        result += string[i]
    return result