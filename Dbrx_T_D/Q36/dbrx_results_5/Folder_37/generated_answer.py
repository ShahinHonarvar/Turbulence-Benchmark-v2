def filter_chars(s):
    curated_chars = [char for char in s if char > '/' and char < '6']
    return ''.join(curated_chars)