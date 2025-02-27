def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (81 <= s.index(char) < 89 and 'f' < char < '{')]
    return ''.join(filtered_chars)