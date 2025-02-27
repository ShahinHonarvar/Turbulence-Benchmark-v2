def filter_chars(string):
    for char in range(318, 337):
        if string[char] > 'B' and string[char] < 'z':
            string = string.replace(string[char], '')
    return string