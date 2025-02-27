def filter_chars(string):
    filtered_string = ''
    for char in string:
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            string = string.replace(char, '')
        filtered_string += char
    return filtered_string