def filter_chars(arg):
    arg = arg[:54] + ''.join([char for char in arg[54:84] if char >= 'j' and char <= 'v']) + arg[84:]
    return arg