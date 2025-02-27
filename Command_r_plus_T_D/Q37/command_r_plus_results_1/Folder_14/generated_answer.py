def filter_chars(s: str) -> str:
    filtered_chars = [char for i, char in enumerate(s, 1) if i < 35 or i > 98 or char < 'A' or (char > 'b')]
    return ''.join(filtered_chars)