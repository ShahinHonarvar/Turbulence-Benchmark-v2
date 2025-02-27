def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 36 <= idx <= 79 and 'a' <= char <= 'i':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)