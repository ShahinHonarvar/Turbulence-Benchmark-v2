def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (45 <= s.index(char) < 69 and 'W' < char < 'x')]
    return ''.join(filtered_chars)