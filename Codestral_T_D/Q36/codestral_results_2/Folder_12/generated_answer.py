def filter_chars(string):
    filtered_string = ''
    for char in string[32:84]:
        if char > 'm' and char < 'w':
            filtered_string += char
    return string[:32] + string[32:84].replace(filtered_string, '') + string[84:]