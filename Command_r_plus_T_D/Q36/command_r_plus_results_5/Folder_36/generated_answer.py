def filter_chars(s: str) -> str:
    filter_range = range(283, 484)
    filtered_chars = [char for i, char in enumerate(s) if i not in filter_range or not 'l' < char < 't']
    return ''.join(filtered_chars)