def filter_chars(str):
    filtered = str[:61] + ''.join([char for char in str[61:71] if char < '@' and char >= '0'] + str[71:])
    return filtered