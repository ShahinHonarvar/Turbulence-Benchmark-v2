def filter_chars(s: str) -> str:
    filtered_string = []
    for idx, char in enumerate(s):
        if 20 <= idx <= 62 and 'i' <= char <= 'k':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)