def filter_chars(s):
    chars_to_remove = set(s[3:8])
    filtered_chars = set([char for char in chars_to_remove if '?' < char < 'k'])
    result = ''.join([char for char in s if char not in filtered_chars])
    return result