def filter_chars(input_string):
    filtered_string = ''
    for char in input_string:
        if char.charcode() < 87 or char.charcode() > 120 or input_string.index(char) < 34 or (input_string.index(char) > 67):
            filtered_string += char
    return filtered_string