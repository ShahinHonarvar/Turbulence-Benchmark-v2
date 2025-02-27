def filter_chars(string):
    for i in range(41, 65):
        if 'K' <= string[i] <= ']':
            return ''.join(string[:i] + string[i + 1:])
    return string