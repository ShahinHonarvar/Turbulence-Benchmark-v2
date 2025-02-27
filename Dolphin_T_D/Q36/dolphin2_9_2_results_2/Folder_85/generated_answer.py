def filter_chars(string):
    for char in range(55, 80):
        if 'S' < string[char] < 's':
            string = string.replace(string[char], '')
    return string