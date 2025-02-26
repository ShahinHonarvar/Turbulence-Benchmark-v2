def filter_chars(string):
    to_remove = set()
    for i in range(2, 7):
        if i < len(string) and '3' < string[i] < '^':
            to_remove.add(string[i])
    return ''.join((char for char in string if char not in to_remove))