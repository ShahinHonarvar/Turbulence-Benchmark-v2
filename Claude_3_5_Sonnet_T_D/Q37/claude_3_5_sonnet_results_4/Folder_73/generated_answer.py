def filter_chars(string):
    chars_to_remove = set()
    for i in range(22, 86):
        if i < len(string) and '7' <= string[i] <= 'e':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))