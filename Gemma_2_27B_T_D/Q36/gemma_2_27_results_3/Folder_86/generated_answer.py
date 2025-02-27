def filter_chars(string):
    for i in range(672, 709):
        char = string[i]
        if char > 'X' and char < '}':
            string = string.replace(char, '')
    return string