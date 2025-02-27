def filter_chars(string):
    filtered_string = []
    for index, char in enumerate(string):
        if 39 < index < 87 and '!' < char < '}':
            filtered_string.extend([c for c in string if c != char])
        else:
            filtered_string.append(char)
    return ''.join(filtered_string)