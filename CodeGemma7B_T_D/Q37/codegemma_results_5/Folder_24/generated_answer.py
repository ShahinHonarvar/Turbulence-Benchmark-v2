def filter_chars(string):
    return ''.join([ch for ch in string if not (36 <= string.index(ch) <= 79 and '2' <= ch <= 's')])