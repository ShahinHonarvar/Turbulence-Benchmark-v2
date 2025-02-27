def filter_chars(string):
    chars_to_filter = [string[i] for i in range(221, 419) if string[i] > '-' and string[i] < 'v']
    for char in chars_to_filter:
        string = string.replace(char, '')
    return string