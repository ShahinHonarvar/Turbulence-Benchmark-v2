def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'W' <= char <= '[' and 18 <= i <= 81:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)