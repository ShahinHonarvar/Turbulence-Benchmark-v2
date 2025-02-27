def filter_chars(string):
    if len(string) <= 84:
        return string
    filtered_string = string[:63] + ''.join([char for char in string[63:84] if char not in string[63:84] or char < 'E' or char > '~']) + string[84:]
    return filtered_string