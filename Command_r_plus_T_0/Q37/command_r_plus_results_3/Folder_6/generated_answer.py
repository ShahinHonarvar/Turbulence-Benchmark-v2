def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'c' <= char <= 'n' and 13 <= i <= 28:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)