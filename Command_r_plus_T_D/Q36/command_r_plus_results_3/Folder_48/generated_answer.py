def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (154 < s.index(char) < 222 and 'A' < char < 'f')]
    return ''.join(filtered_chars)