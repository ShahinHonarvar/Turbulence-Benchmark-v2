def filter_chars(s: str) -> str:
    filter_range = ['Y', 's']
    filtered_chars = [char for char in s if char not in range(ord(filter_range[0]), ord(filter_range[1]) + 1)]
    return ''.join(filtered_chars)