def filter_chars(s):
    filtered_chars = [char for char in s if not 'X' < char < '}']
    return ''.join(filtered_chars)