def filter_chars(s: str) -> str:
    filtered_string = []
    for char in s:
        if 73 <= ord(char) < 74:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)