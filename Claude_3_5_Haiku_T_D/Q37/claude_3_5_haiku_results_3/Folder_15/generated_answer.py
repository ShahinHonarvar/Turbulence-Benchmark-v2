def filter_chars(string):
    chars_to_remove = set()
    for i in range(2, 7):
        if i < len(string):
            char = string[i]
            if '?' <= char <= 'f':
                chars_to_remove.add(char)
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result