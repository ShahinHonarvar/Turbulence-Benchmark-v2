def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if not (23 <= i <= 89 and 'w' <= c <= '{'):
            result += c
    return result