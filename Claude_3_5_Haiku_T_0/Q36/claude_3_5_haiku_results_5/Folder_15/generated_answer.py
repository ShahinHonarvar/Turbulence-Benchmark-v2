def filter_chars(s):
    chars_to_remove = set(s[3:7])
    filtered_chars = [char for char in s if char not in chars_to_remove or char <= 'h' or char >= 'k']
    return ''.join(filtered_chars)