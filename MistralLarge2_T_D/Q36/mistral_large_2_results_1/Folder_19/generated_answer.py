def filter_chars(s):
    to_remove = {s[i] for i in range(77, 87) if ';' < s[i] < 'r'}
    return ''.join((char for char in s if char not in to_remove))