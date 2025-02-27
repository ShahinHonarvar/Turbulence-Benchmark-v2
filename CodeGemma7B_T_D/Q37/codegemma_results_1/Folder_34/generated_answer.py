def filter_chars(str):
    filtered_str = ''.join([c for c in str if not (str.index(c) in range(54, 63) and c in ')9')])
    return filtered_str