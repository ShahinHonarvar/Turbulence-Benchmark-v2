def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if 42 <= i <= 97 and '*' <= c <= 'b']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))