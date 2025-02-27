def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 'F' <= char <= 'h' and 19 <= i <= 90:
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)