def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 164 <= i <= 706 and 'O' <= char <= '}':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)