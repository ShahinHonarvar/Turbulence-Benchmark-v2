def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 19 <= i <= 90 and 'F' <= string[i] <= 'h':
            filtered_string += string[i]
    return string.translate(str.maketrans('', '', filtered_string))