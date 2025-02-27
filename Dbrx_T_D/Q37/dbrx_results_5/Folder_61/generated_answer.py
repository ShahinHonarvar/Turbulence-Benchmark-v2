def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i < 5 or i > 6 or ord(string[i]) < ord('G') or (ord(string[i]) > ord('p')):
            filtered_string += string[i]
    return filtered_string