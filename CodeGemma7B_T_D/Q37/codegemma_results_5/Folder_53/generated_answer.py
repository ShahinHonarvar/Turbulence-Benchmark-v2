def filter_chars(string):
    return ''.join([char for char in string[:83] + ''.join([char for char in string[83:100] if char not in '*' <= char <= 'j']) + string[100:]])