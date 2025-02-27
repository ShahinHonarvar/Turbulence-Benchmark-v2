def filter_chars(string):
    chars_to_remove = set()
    for i in range(672, 709):
        char = string[i]
        if 'X' < char < '}':
            chars_to_remove.add(char)
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result