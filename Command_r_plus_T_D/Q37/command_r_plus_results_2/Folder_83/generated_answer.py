def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'K' <= char <= 'z' and 29 <= i <= 79:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)