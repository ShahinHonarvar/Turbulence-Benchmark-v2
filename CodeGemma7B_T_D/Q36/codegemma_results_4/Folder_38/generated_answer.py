def filter_chars(string):
    string = string[:44] + ''.join([x for x in string[44:48] if x not in '+l'] + string[48:])
    return string