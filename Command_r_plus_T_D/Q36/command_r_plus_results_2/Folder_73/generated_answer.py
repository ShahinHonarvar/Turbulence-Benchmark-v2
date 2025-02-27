def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (66 < ord(char) < 90 and '#' < char < 'T')]
    return ''.join(filtered_chars)