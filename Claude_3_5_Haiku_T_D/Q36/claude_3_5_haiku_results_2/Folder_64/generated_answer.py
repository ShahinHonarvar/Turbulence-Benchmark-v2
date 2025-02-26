def filter_chars(string):
    if len(string) <= 2:
        return string
    chars_to_remove = set()
    for i in range(2, 7):
        if '3' < string[i] < '^':
            chars_to_remove.add(string[i])
    result = ''.join((char for char in string if char not in chars_to_remove))
    return result