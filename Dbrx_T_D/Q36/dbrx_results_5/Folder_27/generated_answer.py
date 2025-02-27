def filter_chars(s):
    filtered_chars = [char for char in s if 48 < ord(char) < 75 and '6' < char < '_' or ord(char) <= 48 or 75 <= ord(char)]
    return ''.join(filtered_chars)