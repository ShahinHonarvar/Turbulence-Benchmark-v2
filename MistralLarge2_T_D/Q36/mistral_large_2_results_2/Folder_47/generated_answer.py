def filter_chars(s):
    to_remove = {s[i] for i in range(45, 57) if 'F' < s[i] < 'n'}
    return ''.join((char for char in s if char not in to_remove))