def filter_chars(string):
    for char in range(672, 709):
        if 'X' < string[char] < '}':
            string = string.replace(string[char], '')
    return string