def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 503 or i > 753 or char < '9' or (char > 'w')])