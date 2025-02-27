def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (283 < s.index(char) < 484 and 'l' < char < 't')]
    return ''.join(filtered_chars)