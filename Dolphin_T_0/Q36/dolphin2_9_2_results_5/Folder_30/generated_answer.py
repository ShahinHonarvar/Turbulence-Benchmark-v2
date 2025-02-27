def filter_chars(string):
    chars_to_filter = []
    for i in range(23, 45):
        if '3' < string[i] < 'I':
            chars_to_filter.append(string[i])
    for char in chars_to_filter:
        string = string.replace(char, '')
    return string