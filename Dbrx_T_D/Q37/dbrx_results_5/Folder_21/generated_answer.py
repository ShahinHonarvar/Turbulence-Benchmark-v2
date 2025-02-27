def filter_chars(s):
    filtered_chars = ''
    for i, c in enumerate(s):
        if i < 603 or i > 759 or (c < 'Q' or c > 'h'):
            filtered_chars += c
    return filtered_chars