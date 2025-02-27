def filter_chars(string):
    filtered_string = ''
    for char in string:
        if len(filtered_string) in range(26, 65):
            if ord(char) in range(ord('V'), ord('o') + 1):
                continue
        filtered_string += char
    return filtered_string