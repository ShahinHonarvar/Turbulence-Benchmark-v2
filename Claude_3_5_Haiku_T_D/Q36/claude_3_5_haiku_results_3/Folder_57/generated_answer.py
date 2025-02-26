def filter_chars(s):
    chars_to_remove = set(s[71:74])
    filtered_chars = [char for char in s if char not in chars_to_remove or not 'A' < char < 'U']
    return ''.join(filtered_chars)