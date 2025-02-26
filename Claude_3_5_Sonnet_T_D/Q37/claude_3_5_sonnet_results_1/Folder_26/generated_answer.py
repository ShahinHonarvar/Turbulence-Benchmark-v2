def filter_chars(string):
    chars_to_remove = set()
    for i in range(20, 63):
        if i < len(string) and 'i' <= string[i] <= 'k':
            chars_to_remove.add(string[i])
    return ''.join((char for char in string if char not in chars_to_remove))