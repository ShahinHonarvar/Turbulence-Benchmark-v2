def filter_chars(string):
    to_remove = [string[i] for i in range(86, 93) if '!' <= string[i] <= 's']
    return ''.join([char for char in string if char not in to_remove])