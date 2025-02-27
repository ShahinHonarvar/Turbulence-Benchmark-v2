def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 71 <= idx <= 94 and 'K' <= char <= 'a':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)