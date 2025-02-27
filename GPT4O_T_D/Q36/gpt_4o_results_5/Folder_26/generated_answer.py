def filter_chars(s):
    to_remove = {ch for ch in s[44:83] if ':' < ch < 'Q'}
    return ''.join((char for char in s if char not in to_remove))