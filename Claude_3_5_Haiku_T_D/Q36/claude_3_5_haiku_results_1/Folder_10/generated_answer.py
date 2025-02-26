def filter_chars(string):
    chars_to_remove = set()
    for i in range(36, 60):
        char = string[i]
        if '!' < char < 'B':
            chars_to_remove.add(char)
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result