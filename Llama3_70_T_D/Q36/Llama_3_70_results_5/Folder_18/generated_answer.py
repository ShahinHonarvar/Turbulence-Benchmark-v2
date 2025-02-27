def filter_chars(s):
    chars_to_remove = [char for char in s[587:648] if ',' < char < 'c']
    filtered_s = ''.join([char for char in s if char not in chars_to_remove])
    return filtered_s