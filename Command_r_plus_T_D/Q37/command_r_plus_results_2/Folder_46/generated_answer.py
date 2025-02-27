def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'i' <= char <= 'v' and 11 <= i <= 72:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)