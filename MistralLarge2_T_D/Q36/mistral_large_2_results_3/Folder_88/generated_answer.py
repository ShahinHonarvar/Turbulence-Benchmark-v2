def filter_chars(s):
    chars_to_remove = {s[i] for i in range(78, 81) if 'S' < s[i] < '['}
    return ''.join((char for char in s if char not in chars_to_remove))