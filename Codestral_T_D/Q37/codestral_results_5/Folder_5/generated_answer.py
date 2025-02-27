def filter_chars(string):
    filtered_string = ''.join([char for i, char in enumerate(string) if not (24 <= i <= 82 and '5' <= char < '<')])
    return filtered_string