def filter_chars(string):
    filtered_string = ''.join((char for i, char in enumerate(string) if i < 513 or i > 877 or char < '?' or (char > 'n')))
    return filtered_string