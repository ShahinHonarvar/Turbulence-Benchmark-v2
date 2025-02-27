def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 124 <= idx <= 854 and '9' <= char <= 's':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)