def filter_chars(s):
    chars_to_remove = {s[i] for i in range(90, 97) if 'j' < s[i] < 'w'}
    return ''.join([char for char in s if char not in chars_to_remove])