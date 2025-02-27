def filter_chars(s):
    filtered_chars = [ch for ch in s if 28 <= s.index(ch) <= 65 and 'O' <= ch <= 'd']
    return ''.join([ch for ch in s if ch not in filtered_chars])