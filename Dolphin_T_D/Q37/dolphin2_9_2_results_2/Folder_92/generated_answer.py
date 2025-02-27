def filter_chars(string):
    characters_to_remove = [char for char in string if 4 <= string.index(char) <= 4 and '7' <= char <= 'o']
    return ''.join([char for char in string if char not in characters_to_remove])