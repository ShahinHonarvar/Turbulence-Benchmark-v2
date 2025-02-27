def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 51 <= ord(char) <= 96 and 'X' <= char <= 'p':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)