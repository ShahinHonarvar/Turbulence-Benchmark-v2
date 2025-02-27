def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if i in range(54, 84) and 'j' <= char <= 'v':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)