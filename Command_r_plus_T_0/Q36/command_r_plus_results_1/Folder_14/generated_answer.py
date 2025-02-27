def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (42 <= s.index(char) < 57 and 'Z' < char < 'c')]
    return ''.join(filtered_chars)