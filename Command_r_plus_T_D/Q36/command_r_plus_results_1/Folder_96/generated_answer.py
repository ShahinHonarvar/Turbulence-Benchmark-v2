def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not 38 < s.index(char) < 81 or not '.' < char < '^']
    return ''.join(filtered_chars)