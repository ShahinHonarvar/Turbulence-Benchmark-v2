def filter_chars(s: str) -> str:
    filtered_string = ''.join((char for char in s if not (25 <= ord(char) <= 97 and 'm' <= char <= 'w')))
    return filtered_string