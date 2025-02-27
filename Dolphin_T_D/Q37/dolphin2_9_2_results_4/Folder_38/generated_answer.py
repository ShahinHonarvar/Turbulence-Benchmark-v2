def filter_chars(string):
    filtered_chars = [char for char in string if not ('a' <= char <= 'f' and 24 <= string.index(char) <= 79)]
    return ''.join(filtered_chars)