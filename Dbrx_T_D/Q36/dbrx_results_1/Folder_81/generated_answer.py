def filter_chars(s):
    filtered_chars = [char for char in s if not '5' < char < 'f' or (50 < len(s) - 1) < ord(char) < 76]
    return ''.join(filtered_chars)