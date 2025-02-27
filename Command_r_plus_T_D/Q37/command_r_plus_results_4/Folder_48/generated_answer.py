def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 513 <= s.index(char) <= 877 and '?' <= char <= 'n']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))