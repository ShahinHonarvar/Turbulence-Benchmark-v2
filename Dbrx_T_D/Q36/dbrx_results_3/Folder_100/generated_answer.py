def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 43 < s.index(char) < 69 and 'B' < char < 'r']
    return ''.join(filtered_chars)