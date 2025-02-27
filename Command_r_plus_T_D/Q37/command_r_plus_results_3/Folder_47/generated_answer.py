def filter_chars(s: str) -> str:
    filter_range = s[38:55]
    filter_chars = [char for char in filter_range if ':' <= char <= 'r']
    result = ''.join([char for char in s if char not in filter_chars])
    return result