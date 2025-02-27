def filter_chars(string):
    for char in range(40, 63):
        if string[char] > '7' and string[char] < 'H':
            string = string.replace(string[char], '')
    return string