def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (476 < s.index(char) < 948 and 'b' < char < 'd')]
    return ''.join(filtered_chars)