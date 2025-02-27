def filter_chars(string):
    to_remove = []
    for i in range(515, 539):
        if '+' <= string[i] <= '}':
            to_remove.append(string[i])
    return ''.join([char for char in string if char not in to_remove])