def filter_chars(string):
    new_string = ''
    for char in string:
        if char.isalpha() and ord(char) >= ord('0') and (ord(char) <= ord('k')):
            continue
        else:
            new_string += char
    return new_string