def filter_chars(string):
    for char_index in range(41, 56):
        if string[char_index] > 'Z' and string[char_index] < 'c':
            string = string.replace(string[char_index], '')
    return string