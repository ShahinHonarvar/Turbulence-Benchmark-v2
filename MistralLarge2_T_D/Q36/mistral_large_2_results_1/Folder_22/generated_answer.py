def filter_chars(s):
    to_remove = {s[i] for i in range(55, 84) if ';' < s[i] < 'z'}
    return ''.join((char for char in s if char not in to_remove))