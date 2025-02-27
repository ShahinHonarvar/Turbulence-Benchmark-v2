def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (19 < s.index(char) < 69 and '<' < char < 'C')]
    return ''.join(filtered_chars)