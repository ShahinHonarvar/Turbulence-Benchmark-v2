def filter_chars(string):
    to_remove = [string[i] for i in range(75, 100) if string[i] >= '8' and string[i] <= 'e']
    return ''.join([char for char in string if char not in set(to_remove)])