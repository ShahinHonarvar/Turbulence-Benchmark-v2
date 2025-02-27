def filter_chars(s):
    chars_to_remove = [c for c in s if c >= '7' and c <= 'o']
    for c in chars_to_remove:
        s = ''.join([x for x in s if x != c])
    return s