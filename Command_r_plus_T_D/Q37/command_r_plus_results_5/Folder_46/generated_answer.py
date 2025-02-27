def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if i >= 11 and i <= 72 and ('i' <= char <= 'v'):
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)