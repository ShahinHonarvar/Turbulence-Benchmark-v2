def filter_chars(string):
    filtered_string = ''.join([char for i, char in enumerate(string) if not 18 < i < 64 or not '3' < char < 'B'])
    return filtered_string