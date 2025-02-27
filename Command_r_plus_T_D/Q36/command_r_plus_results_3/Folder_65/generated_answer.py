def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 58 < s.index(char) < 82 or not 'F' < char < 'O']
    return ''.join(filtered_chars)