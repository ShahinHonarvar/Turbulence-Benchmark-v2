def filter_chars(string):
    for i in range(39, 87):
        char_to_filter = string[i]
        if '!' < char_to_filter < '}':
            string = string.replace(char_to_filter, '')
    return string