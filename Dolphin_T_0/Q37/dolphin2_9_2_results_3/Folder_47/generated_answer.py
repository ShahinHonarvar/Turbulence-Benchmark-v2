def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s) if 38 <= i <= 54 and ':' <= c <= 'r']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s