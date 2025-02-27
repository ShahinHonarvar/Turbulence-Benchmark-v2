def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'W' <= char <= 'x' and 34 <= i <= 67:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)