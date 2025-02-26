def filter_chars(string):
    chars_to_remove = set()
    for i in range(71, 74):
        if 'A' < string[i] < 'U':
            chars_to_remove.add(string[i])
    result = ''
    for char in string:
        if char not in chars_to_remove:
            result += char
    return result