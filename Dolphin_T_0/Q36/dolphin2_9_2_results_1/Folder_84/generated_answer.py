def filter_chars(s):
    target_chars = [c for c in s[171:636] if 'c' < c < 's']
    s = ''.join([char for char in s if char not in target_chars])
    return s