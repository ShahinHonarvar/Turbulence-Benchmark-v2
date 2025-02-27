def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if not ('H' <= char <= 'e' and 38 <= s.index(char) <= 69)]
    return ''.join(filtered_chars)