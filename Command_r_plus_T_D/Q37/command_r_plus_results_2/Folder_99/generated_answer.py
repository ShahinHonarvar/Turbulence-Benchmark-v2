def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 373 <= idx <= 901 and 'T' <= char <= 'h':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)