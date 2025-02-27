def filter_chars(input_string):
    filtered_string = ''
    for i, char in enumerate(input_string):
        if i >= 75 and i <= 99 and (ord(char) >= ord('8')) and (ord(char) <= ord('e')):
            continue
        filtered_string += char
    return filtered_string