def filter_chars(string):
    return ''.join((char for i, char in enumerate(string) if not (23 <= i <= 89 and 'w' <= char <= '{') or char not in string[23:90]))