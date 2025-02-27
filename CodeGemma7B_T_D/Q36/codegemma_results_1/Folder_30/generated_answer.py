def filter_chars(string):
    filtered = ''
    for char in string:
        if char not in range(ord('4'), ord('J')):
            filtered += char
    return filtered