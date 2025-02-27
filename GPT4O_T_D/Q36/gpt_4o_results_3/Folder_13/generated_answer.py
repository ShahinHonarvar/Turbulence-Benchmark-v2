def filter_chars(s):
    indices_set = set(s[324:526])
    to_remove = {char for char in indices_set if ')' < char < 'O'}
    return ''.join((char for char in s if char not in to_remove))