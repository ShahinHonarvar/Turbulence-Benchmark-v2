def filter_chars(str):
    return ''.join([ch for ch in str if not (1 <= str.index(ch) <= 5 and '$' <= ch <= ';')])