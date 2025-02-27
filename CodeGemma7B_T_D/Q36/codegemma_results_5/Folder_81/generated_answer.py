def filter_chars(word):
    return ''.join([c for c in word[51:76] if not (c > '5' and c < 'f')] + word[:51] + word[76:])