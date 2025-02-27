def filter_chars(s):
    to_remove = set(s[138:921])
    result = [char for char in s if char not in to_remove or not '6' <= char <= 'A']
    return ''.join(result)