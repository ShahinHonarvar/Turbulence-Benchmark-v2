def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 75 <= i <= 99 and '8' <= char <= 'e':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)