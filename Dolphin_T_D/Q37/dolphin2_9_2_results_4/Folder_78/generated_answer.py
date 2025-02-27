def filter_chars(s):
    filtered_chars = ['8', '9', 'a', 'b', 'c', 'd', 'e']
    new_string = []
    for char in s:
        if char in filtered_chars:
            new_string.append(char)
    return ''.join(new_string)