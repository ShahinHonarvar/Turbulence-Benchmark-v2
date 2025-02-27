def filter_chars(string):
    chars_to_remove = [c for c in string[26:65] if c >= 'V' and c <= 'o']
    string = ''.join([c for c in string if c not in chars_to_remove])
    return string