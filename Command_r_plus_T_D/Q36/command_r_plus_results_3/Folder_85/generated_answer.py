def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 55 < s.index(char) < 80 or not 'S' < char < 's']
    return ''.join(filtered_chars)