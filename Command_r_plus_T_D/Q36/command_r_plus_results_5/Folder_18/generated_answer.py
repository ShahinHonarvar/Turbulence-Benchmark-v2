def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not (587 < s.index(char) < 648 and char > ',' and (char < 'c'))]
    return ''.join(filtered_chars)