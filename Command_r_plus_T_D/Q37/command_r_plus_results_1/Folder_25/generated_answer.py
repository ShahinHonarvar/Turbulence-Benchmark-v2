def filter_chars(s: str) -> str:
    filtered_chars = [char for char in s if 31 <= ord(char) <= 38 and ';' <= char <= 'g']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))