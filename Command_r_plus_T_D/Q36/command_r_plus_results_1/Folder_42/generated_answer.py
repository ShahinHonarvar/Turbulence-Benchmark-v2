def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (42 < s.index(char) < 68 and 't' < char < 'x')]
    return ''.join(filtered_chars)