def filter_chars(s):
    to_remove = [char for char in s[770:971] if '-' <= char <= 'D']
    return ''.join([char for char in s if char not in to_remove])