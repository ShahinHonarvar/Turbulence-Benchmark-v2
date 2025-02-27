def filter_chars(s):
    indices = range(4, 4 + 1)
    chars = [c for c in s if any((c >= '7' and c <= 'o' for i in indices))]
    return ''.join([x for x in s if x not in chars])