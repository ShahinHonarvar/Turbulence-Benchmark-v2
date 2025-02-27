def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 114 <= idx <= 639 and '!' <= char <= 'x':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)