def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 12 <= idx <= 77 and ':' <= char <= 'L':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)