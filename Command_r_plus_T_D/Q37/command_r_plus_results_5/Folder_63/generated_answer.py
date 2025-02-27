def filter_chars(s: str) -> str:
    filtered_string = []
    for i, char in enumerate(s):
        if 42 <= i <= 92 and '/' <= char <= 'a':
            continue
        filtered_string.append(char)
    return ''.join(filtered_string)