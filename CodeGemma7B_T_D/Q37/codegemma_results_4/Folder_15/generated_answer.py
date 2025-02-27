def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i not in range(2, 7) or not (char >= '?' and char <= 'f')])