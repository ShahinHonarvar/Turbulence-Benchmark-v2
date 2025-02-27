def filter_chars(input_str):
    chars_to_filter = [ch for ch in input_str[379:899] if ch >= 'M' and ch <= 'v']
    return ''.join([ch for ch in input_str if ch not in chars_to_filter])