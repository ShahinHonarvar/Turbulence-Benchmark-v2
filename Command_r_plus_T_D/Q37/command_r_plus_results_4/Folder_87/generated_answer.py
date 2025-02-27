def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 18 <= s.index(char) <= 81 and 'W' <= char <= '[']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))