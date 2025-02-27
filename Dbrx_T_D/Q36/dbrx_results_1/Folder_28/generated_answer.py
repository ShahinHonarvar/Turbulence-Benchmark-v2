def filter_chars(s):
    filtered_chars = [char for char in s if 31 < s.index(char) < 73 and (not 'M' < char < 'j')]
    return ''.join(filtered_chars)