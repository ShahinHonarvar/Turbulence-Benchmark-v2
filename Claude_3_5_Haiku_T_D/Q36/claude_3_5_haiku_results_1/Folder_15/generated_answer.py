def filter_chars(s):
    chars_to_remove = set(s[3:7])
    chars_to_remove = [char for char in chars_to_remove if 'h' < char < 'k']
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result