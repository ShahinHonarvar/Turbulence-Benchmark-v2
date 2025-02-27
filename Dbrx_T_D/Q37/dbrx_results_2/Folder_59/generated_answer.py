def filter_chars(s):
    filtered = [char for i, char in enumerate(s) if i not in range(2, 4) or not '5' <= char <= '_']
    return ''.join(filtered)