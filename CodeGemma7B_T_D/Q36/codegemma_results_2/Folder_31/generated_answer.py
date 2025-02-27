def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 14 or i >= 75 or (char <= '9' and char >= 'K')])