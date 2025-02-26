def filter_chars(string):
    chars_to_remove = set()
    for i in range(min(2, len(string))):
        if '*' <= string[i] <= 's':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))