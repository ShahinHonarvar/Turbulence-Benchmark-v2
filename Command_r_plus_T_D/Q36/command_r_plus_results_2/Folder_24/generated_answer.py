def filter_chars(s: str) -> str:
    filter_range = range(10, 16)
    filter_chars = set('t', 'u', 'v')
    new_str = []
    for i, char in enumerate(s):
        if i in filter_range and char in filter_chars:
            continue
        new_str.append(char)
    return ''.join(new_str)