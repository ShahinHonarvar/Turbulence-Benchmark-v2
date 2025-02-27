def filter_chars(s):
    filtered_string = ''
    for char in s:
        if not (57 <= ord(char) <= 96 and char >= '<' and (char <= 'w')):
            filtered_string += char
    return filtered_string