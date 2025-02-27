def filter_chars(s):
    filtered_chars = [ch for ch in s if 20 <= s.index(ch) <= 62 and 'i' <= ch <= 'k']
    return ''.join([ch for ch in s if ch not in filtered_chars])