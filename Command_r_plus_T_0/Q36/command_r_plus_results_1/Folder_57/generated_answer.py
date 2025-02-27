def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 70 < s.index(char) < 75 or not 'A' < char < 'U']
    return ''.join(filtered_chars)