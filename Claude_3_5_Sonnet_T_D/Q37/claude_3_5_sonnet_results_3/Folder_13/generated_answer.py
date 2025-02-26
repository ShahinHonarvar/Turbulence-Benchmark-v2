def filter_chars(string):
    chars_to_remove = set()
    for i in range(124, 855):
        if i < len(string) and '9' <= string[i] <= 's':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))