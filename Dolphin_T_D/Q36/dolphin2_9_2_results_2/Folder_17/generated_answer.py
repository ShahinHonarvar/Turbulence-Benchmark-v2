def filter_chars(s):
    """Remove all occurrences of any character greater than 'K' and smaller than 'a' in the given string."""
    for char in s[18:95]:
        if 'K' < char < 'a':
            s = ''.join([c for c in s if c != char])
    return s