def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 20 <= i <= 79 and '!' <= char <= 'T':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)